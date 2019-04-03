from django.core.management.base import BaseCommand, CommandError
from UserProfile.models import Authenticator

class Command(BaseCommand):
	def handle(self, *args, **options):
		Authenticator.objects.filter(date_created__week_day__gte=1).delete() #says to delete queries where day of the week = sunday