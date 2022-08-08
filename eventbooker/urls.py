from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('<slug:slug>/', views.EventView.as_view(), name='event'),
    path('booking/<slug:slug>', views.TimeslotAttendance.as_view(),
         name='booking'),
]