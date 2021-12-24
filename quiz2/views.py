from .models import Quiz, Question
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import Quiz, Question
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView

class QuizView(APIView):
    permissions_classses = [IsAuthenticated, ]
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get(self, request, id):
        quiz = get_object_or_404(Quiz, id=id)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)

    def put(self, request, id):
        quiz = get_object_or_404(Quiz, id=id)
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            update_fields = []
            for field, value in serializer.validated_data.items():
                setattr(quiz, field, value)
                update_fields.append(field)
            quiz.save(update_fields=update_fields)

            serializer = QuizSerializer(instance=quiz)
            return Response(serializer.data)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        spending = get_object_or_404(Quiz, id=id, author=self.request.user)
        spending.delete()
        return Response({'detail': 'success'}, status=status.HTTP_204_NO_CONTENT)

class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)
    

class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz_question = Question.objects.filter(quiz__title__name=kwargs['topic']).order_by('?')[:1]
        serializer = QuestionSerializer(quiz_question, many=True)
        return Response(serializer.data)

    def put(self, request, id):
        quiz_question = get_object_or_404(Question, id=id)
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            update_fields = []
            for field, value in serializer.validated_data.items():
                setattr(quiz_question, field, value)
                update_fields.append(field)
            quiz_question.save(update_fields=update_fields)

            serializer = QuestionSerializer(instance=quiz_question)
            return Response(serializer.data)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        spending = get_object_or_404(Question, id=id, owner=self.request.user)
        spending.delete()
        return Response({'detail': 'success'}, status=status.HTTP_204_NO_CONTENT)




