import pytz

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

#code to take care of timezones - based on https://docs.djangoproject.com/en/1.10/topics/i18n/timezones/


class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()