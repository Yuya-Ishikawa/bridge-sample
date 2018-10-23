from django.urls import path
from . import views 

urlpatterns = [
    path('', views.contactPage, name='contactPage'),
    path('<article>', views.articlePage, name='contact-articlePage'),

]

