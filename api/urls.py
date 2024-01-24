from django.urls import path
from .apiviews import BookAPIView


urlpatterns = [
    path('',BookAPIView.as_view())
]

