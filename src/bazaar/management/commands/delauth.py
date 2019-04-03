from UserProfile.models import Authenticator
Authenticator.objects.filter(date_created__week_day__gte=1).delete() #says to select queries where day of the week = monday