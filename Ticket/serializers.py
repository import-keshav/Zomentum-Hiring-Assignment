from rest_framework import serializers

from . import models as ticket_models
from User import serializers as user_serializer


class CreateDeleteTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket_models.Ticket
        fields = '__all__'


class ListTicketSerializer(serializers.ModelSerializer):
    user = user_serializer.UserSerializer()
    class Meta:
        model = ticket_models.Ticket
        fields = '__all__'
