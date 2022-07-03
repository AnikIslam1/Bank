from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('users/', views.Account_User.as_view()),
    path('users/<int:pk>', views.Account_Details.as_view()),
    path('history/', views.History_User.as_view()),
    path('history/<int:pk>', views.History_Details.as_view()),
]