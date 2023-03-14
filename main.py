import os

import django
from django.utils import timezone
import datetime as dt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit  # noqa: E402

if __name__ == '__main__':
    def get_duration(visit_):
        """Вернет длительность нахождения для визита хранилища"""
        visitor_entered_time = visit_.entered_at
        visitor_leaved_at = visit_.leaved_at
        try:
            if visitor_leaved_at:
                delta = visitor_leaved_at - visitor_entered_time
                return delta
        except visit_.DoesNotExist:
            return None

    def is_visit_suspect(visit_time_in_vault, mins):
        """Проверит визит на подозрительность и вернет подозрительный визит"""
        try:
            if visit_time_in_vault > dt.timedelta(minutes=mins):
                return True
        except TypeError:
            return None

    visitor_history = Visit.objects.filter(passcard__owner_name='Julie Brown')
    suspect_visits_total = []

    for visit in visitor_history:
        duration = get_duration(visit)
        is_suspect = is_visit_suspect(duration, 60)
        if is_suspect:
            suspect_visits_total.append(visit)
    print(suspect_visits_total)

