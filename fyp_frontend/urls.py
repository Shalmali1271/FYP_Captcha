from django.urls import path
 
# importing views from views..py
from .views import index, success
 
urlpatterns = [
    path('', index),
    path('success/', success, name="success"),
]