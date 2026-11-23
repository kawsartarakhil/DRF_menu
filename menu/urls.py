from django.urls import path
from .views import *

urlpatterns = [
    path('categories/',Category_View.as_view()),
    path('categories/<int:pk>/',Category_Detail.as_view()),
    path('dishes/',Dish_View.as_view()),
    path('dishes/<int:pk>/',Dish_Detail.as_view()),
    path('orders/',Order_View.as_view()),
    path('orders/<int:pk>/',Order_Detail.as_view()),
    path('orders/update/<int:pk>/',Order_Update.as_view()),
]