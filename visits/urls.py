from django.urls import path
from . import views

#Urls Configuration
urlpatterns = [
    path('', views.vistis_view),
]