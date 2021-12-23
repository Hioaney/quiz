from django.urls import path

from accounts.views import TopUsersView
from .views import  QuizView, RandomQuestion, QuizQuestion



urlpatterns = [
    path('quizzes', QuizView.as_view()),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random' ),
    path('quizzes/questions/<str:topic>/', QuizQuestion.as_view(), name='questions' ),
]