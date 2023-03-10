import os

import django
from django.utils import timezone
import datetime as dt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit  # noqa: E402

if __name__ == '__main__':

    visitor_in_vault = Visit.objects.filter(leaved_at__isnull=True)
    visitor_entered_local_time = django.utils.timezone.localtime(visitor_in_vault[0].entered_at)
    visitor_entered_utc_time = visitor_in_vault[0].entered_at
    now_time = dt.datetime.utcnow()
    delta_time = visitor_entered_utc_time - now_time


    print(f'Зашёл в хранилище, время по Москве: {os.linesep}'
          f'{visitor_entered_local_time}'
          f'{os.linesep}'
          f'Находится в хранилище: {os.linesep}'
          f'{visitor_entered_utc_time} {visitor_entered_local_time} {now_time} {delta_time}')

    # a = datetime.date("%Y/%m/%d-%H.%M.%S")
    # print(a)
