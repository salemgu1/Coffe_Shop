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

    path('admin-view-product', views.admin_view_product_view, name='admin-view-product'),
    path('delete-product/<int:pk>', views.delete_product_view, name='delete-product'),

    path('adminlogin', LoginView.as_view(template_name='multiplex/adminlogin.html'), name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    path('admin-product', views.admin_product_view, name='admin-product'),
    path('admin-add-product', views.admin_add_product_view, name='admin-add-product'),
    path('admin-feedback', views.admin_feedback_view, name='admin-feedback'),

    path('customer-home', views.customer_home_view, name='customer-home'),
    path('customer-home/<order_by>/', views.customer_home_view, name='customer-home'),
    path('customer-dashboard', views.customer_dashboard_view, name='customer-dashboard'),
    path('customer-profile', views.customer_profile_view, name='customer-profile'),
    path('edit-customer-profile', views.edit_customer_profile_view, name='edit-customer-profile'),
    path('customer-feedback', views.customer_feedback_view, name='customer-feedback'),
    path('customer-ticket', views.customer_ticket_view, name='customer-ticket'),
    path('view-product-details/<int:pk>', views.view_product_details_view, name='view-product-details'),

    path('buy-now/<int:pk>', views.buy_now_view, name='buy-now'),
    path('choose-seat', views.choose_seat_view, name='choose-seat'),
    path('proceed-to-pay', views.proceed_to_pay_view, name='proceed-to-pay'),
    path('payment-success', views.payment_success_view, name='payment-success'),

    path('logout', LogoutView.as_view(template_name='multiplex/logout.html'), name='logout'),
]
