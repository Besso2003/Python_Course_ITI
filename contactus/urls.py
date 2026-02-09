from django.urls import path
from contactus.views import contact_page

app_name = 'contactus'

urlpatterns = [
    path('', contact_page, name='contact'),
]