from django.urls import path
from . import views 

urlpatterns = [
    path('', views.sponsorshipPage, name='sponsorshipPage'),
    path('<article>', views.articlePage, name='sponsorship-articlePage'),
]
