from django.urls import path
from . import views

#Urls Configuration
urlpatterns = [
    path('', views.vistis_view),
    path('data', views.visits_view_all_data),
]