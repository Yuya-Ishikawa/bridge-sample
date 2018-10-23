from django.urls import path
from . import views 

urlpatterns = [
    path('', views.usefulPage, name='usefulPage'),
    path('<article>', views.articlePage, name='useful-articlePage'),
]
