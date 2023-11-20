from app1.views import *
from django.urls import path
app_name = 'nothing'
urlpatterns=[
    path('yuvaraj/', yuvaraj, name='yuvaraj'),
    path('sachin/',sachin, name='sachin'),
]