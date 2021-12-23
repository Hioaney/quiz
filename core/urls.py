from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from accounts.views import UserView, TopUsersView
from quiz2.views import QuizView, QuizQuestion


schema_view = get_schema_view(
   openapi.Info(
      title="QUIZ API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/quizzes/', include('quiz2.urls')),
   path('rest-auth/', include('rest_auth.urls')),
   path('api/swagger/', schema_view.with_ui(), name='schema-json'),
   path('api/v2/top-users/', TopUsersView.as_view(), name='top_users_url'),
   path('api/v2/quizzes/<int:id>/', QuizView.as_view(), name='quizzes_url'),
   path('api/v1/quiz-questions/', QuizQuestion.as_view()),
   path('api/v1/user/<int:id>/', UserView.as_view()),

]