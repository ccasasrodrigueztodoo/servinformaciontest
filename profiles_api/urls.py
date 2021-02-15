from django.urls import path
from profiles_api import views

urlpatterns = [
    path('api-profiles/', views.ApiProfileView.as_view()),

]