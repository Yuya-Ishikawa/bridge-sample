from django.urls import path
from . import views 

urlpatterns = [
    path('', views.aboutPage, name='aboutPage'),
    path('<article>', views.articlePage, name='about-articlePage'),
]

