import imp
from re import A
from django.urls import path
from .views import EventsView,EventDetail
from . import views

app_name= 'organization'

urlpatterns = [
      path('organization_auth/',views.organization_auth , name='organization_auth'),
      path('organization_home/',views.organization_home , name='organization_home'),
      path('organization_profile/',views.organization_profile , name='organization_profile'),
      path('organization_event/',views.organization_event , name='organization_event'),
      path('eventform/',views.eventform , name='eventform'),
      path('eventlist/', EventsView.as_view(), name='event_list'),
      path('eventdetail/<int:pk>/', EventDetail.as_view(),name= 'event_detail'),   
]
