from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('users/', views.Account.as_view()),
    path('users/<int:pk>', views.Account_Details.as_view()),
]