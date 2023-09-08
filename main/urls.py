from django.urls import path

from main.views import OreSampleCreateView, OreSampleStatsView

urlpatterns = [
    path('create/', OreSampleCreateView.as_view()),
    path('stats/', OreSampleStatsView.as_view()),
    ]