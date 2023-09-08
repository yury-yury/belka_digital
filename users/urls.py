from django.urls import path

from users.views import UserCreateView, LoginView

urlpatterns = [
    path('signup', UserCreateView.as_view()),
    path('login', LoginView.as_view()),
]
