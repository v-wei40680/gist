# django-statistics.py

"""
使用django的ORM框架按月统计近一年内的数据方法
"""

import datetime
from dateutil.relativedelta import relativedelta

from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import (
  ExtractMonth, ExtractYear
)
from app.models import Trade

# 计算时间
time_ago = datetime.datetime.now() - relativedelta(years=1)
# 获取近一年数据
one_year_data = Data.objects.filter(create_time__gte=time_ago)
# 分组统计每个月的数据
count_res = one_year_data\
            .annotate(year=ExtractYear('create_time'),month=ExtractMonth('create_time'))\
      .values('year', 'month').order_by('year', 'month').annotate(count=Count('id'))
print(count_res)

url = "https://www.jb51.net/article/165680.htm"

def trade_list(request, year, month):
  trades = Trade.objects.filter(createTime__year=year, createTime__month=month)
  month_res = trades.annotate(day=ExtractDay('createTime')).values('day').order_by('day')\
      .annotate(count=Count('id'))
  data = list(month_res)

  return JsonResponse({'month_res': data})
  
urlpatterns = [
  path('trades/<int:year>/<int:month>/', trade_list)
]
