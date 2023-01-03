from django.urls import path
from . import views

urlpatterns = [
    path("concerts/", views.ConcertList.as_view()),
    path("concerts/<int:pk>", views.ConcertDetail.as_view()),
]
