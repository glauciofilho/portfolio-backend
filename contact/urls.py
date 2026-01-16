from django.urls import path
from .views import send_contact_message

urlpatterns = [
    path('form/', send_contact_message, name='contact'),
]