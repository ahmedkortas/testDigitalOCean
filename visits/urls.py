from django.urls import path
from . import views

#Urls Configuration
urlpatterns = [
    path('VisitActivity', views.VisitActivity),
    # path('data', views.visits_view_all_data),
    path('excel', views.generateExcelForAVisit),
    path('users', views.getUsers),
    path('allVisitsForUser', views.allVisitsForUser),
    path('VisitActvityAndResults', views.VisitActvityAndResults),
    path('training', views.tr),
]