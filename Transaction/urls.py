from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('users/', views.User.as_view()),
    path('users/<int:pk>', views.Customer_Details.as_view()),
]