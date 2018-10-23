from django.urls import path
from . import views 

urlpatterns = [
    path('', views.reportPage, name='reportPage'),
    path('<article>', views.articlePage, name='report-articlePage'),
]
