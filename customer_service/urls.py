from django.urls import path
from . import views

urlpatterns = [
    path('submit-request/', views.submit_request, name='submit_request'),
    path('request-status/', views.request_status, name='request_status'),
    path('success/', views.success, name='success'),
]
