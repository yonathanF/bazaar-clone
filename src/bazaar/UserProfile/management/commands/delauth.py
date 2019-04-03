from django.core.management.base import BaseCommand, CommandError
from UserProfile.models import Authenticator

class Command(BaseCommand):
	def handle(self, *args, **options):
		while(1):
			Authenticator.objects.filter(date_created__week_day__gte=4).delete() #says to delete queries where day of the week = sunday