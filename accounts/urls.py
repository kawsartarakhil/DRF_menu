from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/',Register_View.as_view()),
    path('login/',Login_View.as_view()),
    path('logout/',Logout_View.as_view()),
    path('profile/',Profile_View.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
]