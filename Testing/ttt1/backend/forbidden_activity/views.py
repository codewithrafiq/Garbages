import json
from datetime import datetime
from traceback import print_tb
from cv2 import pencilSketch
from django.http import HttpResponse
from forbidden_activity.models import *
from .serializers import *
from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
import pytz
from django.db import connection
from rest_framework import permissions, authentication
from dateutil.parser import parse
from django.utils.timezone import make_aware
from django.db.models import Count
from django.db.models import Sum
from django.db.models import Q

cursor = connection.cursor()
"""
    >>> from django.db import connection
    >>> cursor = connection.cursor()
    >>> cursor.execute('''SELECT count(*) FROM people_person''')

SELECT COUNT( person ), date_format(time, '%Y-%m-%d %H') AS my_date FROM entry GROUP BY my_date;
SELECT COUNT( person ), date_format(time, '2021-01-01 %H') AS my_date FROM entry GROUP BY my_date;

"""


def entryEnter(request):
    with open('data.json', 'r') as f:
        data = json.load(f)
        for d in data:
            entry = ForbiddenActivity(
                date_time=d["created_at"],
                worker_uuid=d["worker_id"],
                activity=Activity.objects.get(id=d["activity_id"]),
                total_time=d["total_time"],
            )
            entry.save()
    return HttpResponse("OK")


class Chart1(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [authentication.TokenAuthentication, ]

    def post(self, request):
        print("date---------------------->", request.data)
        try:
            date = request.data['date']
            present_time = f"{date} 08:30:00"
            last_time = f"{date} 09:00:00"

            floor_total_worker = Floor.objects.first().total_worker

            total_entry = Entry.objects.filter(time__icontains=date).filter(
                time__lte=last_time).aggregate(Sum('person'))
            on_time_entry = Entry.objects.filter(time__icontains=date).filter(time__lte=present_time).aggregate(Sum('person'))
            late_entry = Entry.objects.filter(time__icontains=date).filter(time__gt=present_time).filter(
                time__lte=last_time).aggregate(Sum('person'))
            
            total_entry = total_entry['person__sum'] if total_entry['person__sum'] != None else 0
            total_absent = floor_total_worker - total_entry
            
            all_data = {
                'on_time_entry': on_time_entry['person__sum'] if on_time_entry['person__sum'] else 0,
                'late_entry': late_entry['person__sum'] if late_entry['person__sum'] else 0,
                'total_absent': total_absent if total_absent else 0,
                'total_worker': floor_total_worker if floor_total_worker else 0
            }
            print("all_data----->", all_data)
            return Response([all_data])
        except Exception as e:
            print("error----->", e)
            return Response({"error": str(e)})


class Chart2(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [authentication.TokenAuthentication, ]

    def post(self, request):
        date = request.data['date']
        date1 = date.split('-')
        present_time = f"{date} 08:30:00"
        # The starting time of the day.
        start_time_sum = f"{date} 07:00:00"
        last_time_sum0 = f"{date} 08:00:00"
        last_time_sum1 = f"{date} 09:00:00"

        start_time_rt = f"{date} 06:00:00"
        last_time_rt = f"{date} 18:00:00"

        # time1 = " 08:00:00"
        # date_time1 = date+time1

        # time2 = " 08:59:00"
        # date_time2 = date+time2
        # # q = Entry.objects.raw(f"""SELECT COUNT( person ), date_format(time, '2022-03-14 %H') AS my_date FROM entry GROUP BY my_date""")
        # # q = Entry.objects.values('time').annotate(Count('person')).filter(time__contains=date)
        # # q = Entry.objects.values("time").annotate(Count('person')).filter(Q(time__gte=date_time1) & Q(time__lt=date_time2))

        # entry_by_date_and_hour = Entry.objects.filter(time__year=date[0],time__month=date[1],time__day=date[2]).values('time__hour').annotate(Count('person')).order_by('time__minute')
        # exit_by_date_and_hour = Exit.objects.filter(time__year=date[0],time__month=date[1],time__day=date[2]).values('time__hour').annotate(Count('person')).order_by('time__minute')

        entry_sum0 = Entry.objects.filter(
            time__gte=start_time_sum, time__lte=last_time_sum0).aggregate(Sum('person'))
        entry_sum1 = Entry.objects.filter(
            time__gte=start_time_sum, time__lte=last_time_sum1).aggregate(Sum('person'))
        rt_entry_dhm = Entry.objects.filter(time__gte=start_time_rt, time__lte=last_time_rt).values(
            'time__hour', 'time__minute').annotate(Sum('person')).order_by('time__hour', 'time__minute')
        rt_exit_dhm = Exit.objects.filter(time__gte=start_time_rt, time__lte=last_time_rt).values(
            'time__hour', 'time__minute').annotate(Sum('person')).order_by('time__hour', 'time__minute')
        # difference_between_entry_and_exit_query_by_minute
        return Response({
            # "entry_sum": entry_sum0,
            "entry_sum": [{"person__sum": 0}, entry_sum0, entry_sum1],
            "rt_entry_dhm": rt_entry_dhm
        })


class Chart345(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = [authentication.TokenAuthentication, ]

    def post(self, request):
        date = request.data['date']
        time = request.data['time']  # 24 Hour and minute ---> "11:30:00"
        if int(time.split(':')[0]) >= 18:
            time = "18:00:00"
            print("time----->", int(time.split(':')[0]), time)
        start_time = f"{date} 07:00:00"
        last_time_sum = f"{date} 09:00:00"
        date_s = date.split('-')

        entry_sum = Entry.objects.filter(
            time__gte=start_time, time__lte=last_time_sum).aggregate(Sum('person'))
        exit_sum = Exit.objects.filter(
            time__gte=start_time, time__lte=last_time_sum).aggregate(Sum('person'))

        entry_sum['person__sum'] = 0 if entry_sum['person__sum'] == None else entry_sum['person__sum']
        exit_sum['person__sum'] = 0 if exit_sum['person__sum'] == None else exit_sum['person__sum']

        # on_time_entry_sum = Entry.objects.filter(
        #     time__gte=start_time, time__lte=f'{date} {time}').aggregate(Sum('person'))
        # on_time_exit_sum = Exit.objects.filter(
        #     time__gte=start_time, time__lte=f'{date} {time}').aggregate(Sum('person'))

        # on_time_entry_sum['person__sum'] = 0 if on_time_entry_sum['person__sum'] == None else on_time_entry_sum['person__sum']
        # on_time_exit_sum['person__sum'] = 0 if on_time_exit_sum['person__sum'] == None else on_time_exit_sum['person__sum']

        # on_time_current_worker = on_time_entry_sum['person__sum'] - on_time_exit_sum['person__sum']

        # System Loss
        current_worker = entry_sum['person__sum'] - \
            exit_sum['person__sum']  # current_worker
        defined_worker_minute = (current_worker * 11) * \
            60  # actual_worker_minute

        total_system_loss_ms = ForbiddenActivity.objects.filter(
            date_time__year=date_s[0], date_time__month=date_s[1], date_time__day=date_s[2]).aggregate(Sum('total_time'))  # total_system_loss_ms

        # total_system_loss_minute
        total_system_loss_ms['total_time__sum'] = 0 if total_system_loss_ms[
            'total_time__sum'] == None else total_system_loss_ms['total_time__sum']
        total_system_loss_minute = (
            total_system_loss_ms['total_time__sum'] / 6e+7)

        # total_used_minute = (
        #     actual_worker_minute - total_system_loss_minute) # total_used_minute

        # On time System Loss Calculation

        on_time_time_diff = datetime.strptime(
            time, '%H:%M:%S') - datetime.strptime('07:00:00', '%H:%M:%S')
        on_time_diff_mnt = int(on_time_time_diff.seconds / 60)

        # if on_time_diff_mnt >= defined_worker_minute:
        #     on_time_diff_mnt = defined_worker_minute

        on_time_worker_minute = current_worker * int(on_time_diff_mnt)

        # on_time_system_loss_ms = ForbiddenActivity.objects.filter(created_at__gte=start_time, created_at__lte=f"{date} {time}").aggregate(Sum('total_time'))  # on_time_system_loss_ms
        on_time_system_loss_ms = ForbiddenActivity.objects.filter(
            date_time__icontains="2022-03-16").aggregate(Sum('total_time'))  # on_time_system_loss_ms

        print("on_time_system_loss_ms----->", on_time_system_loss_ms)

        on_time_system_loss_ms['total_time__sum'] = 0 if on_time_system_loss_ms[
            'total_time__sum'] == None else on_time_system_loss_ms['total_time__sum']
        on_time_system_loss_minute = (
            on_time_system_loss_ms['total_time__sum'] / 6e+7)

        on_time_actual_worker_minute = on_time_worker_minute - 32
        print("on_time_actual_worker_minute----->", on_time_actual_worker_minute)
        if current_worker < 0:
            return Response({
                "message": "No Worker Found",
                "on_time_actual_worker_minute": on_time_actual_worker_minute,
            })

        # System Loss Percentage
        on_time_system_loss_percentage = (
            on_time_system_loss_minute/on_time_actual_worker_minute) * 100  # system_loss_percentage

        # System Loss Factors
        # Chart 3 Start

        system_loss_by_activity = ForbiddenActivity.objects.filter(
            date_time__year=date_s[0], date_time__month=date_s[1], date_time__day=date_s[2]).values('activity').annotate(Sum("total_time"))

        for slba in system_loss_by_activity:
            slba["total_time__sum"] = slba["total_time__sum"] / 6e+7
            slba["activity"] = Activity.objects.get(id=slba["activity"]).title

        # Chart 3 End

        # print("system_loss_by_activity----->", system_loss_by_activity)

        # Chart 4 Start

        system_loss_by_activity_chart5 = ForbiddenActivity.objects.filter(
            date_time__year=date_s[0], date_time__month=date_s[1], date_time__day=date_s[2]).values('activity', "date_time__hour").annotate(Count("total_time")).order_by('date_time__hour')

        for slba in system_loss_by_activity_chart5:
            slba["activity"] = Activity.objects.get(id=slba["activity"]).title

        print("system_loss_by_activity_chart5----->",
              system_loss_by_activity_chart5)

        # Chart 4 End

        response_data = {
            "chart3": 
                {
                    "defined_worker_minute": defined_worker_minute,
                    "on_time_worker_minute": on_time_worker_minute-on_time_system_loss_minute,
                    "on_time_system_loss_minute": on_time_system_loss_minute,
                    "on_time_system_loss_percentage": on_time_system_loss_percentage
                },
            "chart4": system_loss_by_activity,
            "chart5": system_loss_by_activity_chart5
        }

        print("response_data----->",response_data)

        return Response(response_data)


class DetailsView(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    # authentication_classes = [authentication.TokenAuthentication, ]

    def get(self, request):
        date = "2022-03-16"
        # date = request.data['date']
        emply_activaty_by_activaty = ForbiddenActivity.objects.exclude(worker_uuid=None).filter(date_time__icontains=date).values('worker_uuid').annotate(Count("activity")).order_by('worker_uuid')

        per_worker_activity = {}
        for worker in emply_activaty_by_activaty:
            per_worker_activity[worker["worker_uuid"]] = ForbiddenActivity.objects.filter(worker_uuid=worker["worker_uuid"]).values('activity').annotate(Sum("total_time"))
            for activity in per_worker_activity[worker["worker_uuid"]]:
                activity["activity"] = Activity.objects.get(id=activity["activity"]).title
                activity["total_time__sum"] = activity["total_time__sum"] / 6e+7


        return Response(per_worker_activity)
