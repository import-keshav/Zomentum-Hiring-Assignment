from datetime import datetime
from django_cron import CronJobBase, Schedule
from . import models as ticket_models


class DeleteExpiredTicketsJob(CronJobBase):
	RUN_EVERY_MINS = 1
	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'Ticket_DeleteExpiredTicketsJob'

	def do(self):
		tickets = ticket_models.Ticket.objects.all()
		for ticket in tickets:
			if ticket.is_expired:
				ticket.delete()
			else:
				current_time = datetime.now()
				current_time =  current_time.strftime("%H:%M:%S")
				time_delta = datetime.strptime('23:00:00', '%H:%M:%S') - datetime.strptime(str(ticket.show.start_time), '%H:%M:%S')
				if time_delta.seconds > 28800:
					ticket.is_expired = True
					ticket.save()
