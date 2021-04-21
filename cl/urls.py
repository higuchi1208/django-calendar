from django.urls import path
from . import views

app_name = 'cl'

urlpatterns = [
  path('', views.CalendarView.as_view(), name="calendar"),
  path('event/new/', views.event, name="event_new"),
  path('event/edit/(?<event_id>\d+)/', views.event, name="event_edit"),
  path('eventdelete/<event_id>/', views.EventDelete.as_view(), name="eventdelete"),
  
]