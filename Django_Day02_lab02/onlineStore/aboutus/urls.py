from django.urls import path
from aboutus.views import about_page

app_name = 'aboutus'

urlpatterns = [
    path('', about_page, name='about')
]