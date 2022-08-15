from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('my_bookings/', views.BookingsView.as_view(), name='my_bookings'),
    path('<slug:slug>/', views.EventView.as_view(), name='event'),
    path('booking/<slug:slug>/<int:pk>', views.TimeslotAttendance.as_view(),
         name='timeslot_booking'),
]