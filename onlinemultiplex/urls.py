from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from multiplex import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),

    path('adminclick', views.adminclick_view),

    path('afterlogin', views.afterlogin_view, name='afterlogin'),

    path('customersignup', views.customer_signup_view, name='customersignup'),
    path('customerlogin', LoginView.as_view(template_name='multiplex/customerlogin.html'), name='customerlogin'),

    path('admin-customer', views.admin_customer_view, name='admin-customer'),
    path('admin-view-customer', views.admin_view_customer_view, name='admin-view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view, name='delete-customer'),
    path('admin-add-customer', views.admin_add_customer_view, name='admin-add-customer'),
    path('admin-view-customer-booking', views.admin_view_customer_booking_view, name='admin-view-customer-booking'),
    path('delete-booking/<int:pk>', views.delete_booking_view, name='delete-booking'),
    path('cancel-ticket/<int:pk>', views.cancel_ticket_view, name='cancel-ticket'),

    path('admin-view-movie', views.admin_view_movie_view, name='admin-view-movie'),
    path('delete-movie/<int:pk>', views.delete_movie_view, name='delete-movie'),

    path('adminlogin', LoginView.as_view(template_name='multiplex/adminlogin.html'), name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    path('admin-movie', views.admin_movie_view, name='admin-movie'),
    path('admin-add-movie', views.admin_add_movie_view, name='admin-add-movie'),
    path('admin-feedback', views.admin_feedback_view, name='admin-feedback'),

    path('customer-home', views.customer_home_view, name='customer-home'),
    path('customer-home/<order_by>/', views.customer_home_view, name='customer-home'),
    path('customer-dashboard', views.customer_dashboard_view, name='customer-dashboard'),
    path('customer-profile', views.customer_profile_view, name='customer-profile'),
    path('edit-customer-profile', views.edit_customer_profile_view, name='edit-customer-profile'),
    path('customer-feedback', views.customer_feedback_view, name='customer-feedback'),
    path('customer-ticket', views.customer_ticket_view, name='customer-ticket'),
    path('view-movie-details/<int:pk>', views.view_movie_details_view, name='view-movie-details'),

    path('book-now/<int:pk>', views.book_now_view, name='book-now'),
    path('choose-seat', views.choose_seat_view, name='choose-seat'),
    path('proceed-to-pay', views.proceed_to_pay_view, name='proceed-to-pay'),
    path('payment-success', views.payment_success_view, name='payment-success'),

    path('logout', LogoutView.as_view(template_name='multiplex/logout.html'), name='logout'),
]
