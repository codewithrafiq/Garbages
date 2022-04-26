from django.urls import path
from .views import *

urlpatterns = [
    # path('entry/', entryEnter, name='index'),
    path('chart1/', Chart1.as_view(), name='chart1'),
    path('chart2/', Chart2.as_view(), name='chart2'),
    path('chart345/', Chart345.as_view(), name='chart345'),
    path('detailsview/', DetailsView.as_view(), name='detailsview'),
]
