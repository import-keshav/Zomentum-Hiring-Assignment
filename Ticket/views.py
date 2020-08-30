from django import forms
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from User import models as user_models
from User import serializers as user_serializer
from Movie import models as movie_models

from . import models as ticket_models
from . import serializers as ticket_serializer


class BookTicket(APIView):
    """     Book A Ticket API   """
    def post(self, request):
        """     POST Request API for booking an API     """
        must_keys = ['name', 'mobile', 'show_id']
        for key in must_keys:
            if not key in self.request.data:
                raise forms.ValidationError("Please include " + key)

        data = self.request.data
        user = (user_models.User.objects.filter(
                mobile=data['mobile']).first())
        if not user:
            user_serializer_obj = (
                user_serializer.UserSerializer(data={
                    'name':data['name'],
                    'mobile': data['mobile']
                }))
            if user_serializer_obj.is_valid():
                user_serializer_obj.save()
                user = (user_models.User.objects.filter(
                    pk=user_serializer_obj.data['id']).first())
            else:
                return Response(
                    user_serializer_obj.errors,
                    status=status.HTTP_400_BAD_REQUEST)

        show = (
            movie_models.MovieShow.objects.filter(
                pk=int(data['show_id'])).first())
        if not show:
            return Response(
                {'message': 'No Show exist with this ID'},
                status=status.HTTP_400_BAD_REQUEST)

        if ticket_models.Ticket.objects.filter(show=show).count() == 20:
            return Response(
                {'message': 'Seats Booked, No ticket available'},
                status=status.HTTP_400_BAD_REQUEST)
        ticket = ticket_models.Ticket(show=show, user=user)
        ticket.save()

        return Response({
            'message': 'Ticket Booked Succesfully',
            'ticket_id': ticket.id
        }, status=status.HTTP_201_CREATED)


class DeleteTicket(generics.DestroyAPIView):
    queryset = ticket_models.Ticket.objects.all()
    serializer_class = ticket_serializer.CreateDeleteTicketSerializer


class GetTicket(generics.ListAPIView):
    serializer_class = ticket_serializer.ListTicketSerializer

    def get_queryset(self):
        return ticket_models.Ticket.objects.filter(pk=self.kwargs['ticket_id'])
