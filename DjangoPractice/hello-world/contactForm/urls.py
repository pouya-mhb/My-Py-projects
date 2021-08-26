from django.urls import path 
from . import views 

#URL Conf
urlpatterns=[
    # path('',views.mhb_response),
    path('register/', views.register),
    path('request-name',views.request_name)
]