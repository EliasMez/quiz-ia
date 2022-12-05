from django.urls import path
from .views import *


urlpatterns = [
    path('quiz', quiz_view, name = "quiz"), 
]
