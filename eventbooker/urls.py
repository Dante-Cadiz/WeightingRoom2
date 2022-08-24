from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('my_bookings/', views.BookingsView.as_view(), name='my_bookings'),
    path('<slug:slug>/', views.EventView.as_view(), name='event'),
    path('booking/<slug:slug>/<int:pk>', views.MakeBooking.as_view(),
         name='make_booking'),
    path('cancel_booking/<slug:slug>/<int:pk>', views.CancelBooking.as_view(),
         name='cancel_booking'),
    #path('edit_comment/<slug:slug>/<int:pk>', views.EditComment.as_view(),
        # name='edit_comment'),
    path('delete_comment/<slug:slug>/<int:pk>', views.DeleteComment.as_view(),
         name='delete_comment'),
]