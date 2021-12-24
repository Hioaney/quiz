from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.db.models import Sum
from .serializers import UserSerializer, TopUserSerializer
from rest_framework.response import Response
from .models import User

User = get_user_model()

class UserView(APIView):

    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            update_fields = []
            for field, value in serializer.validated_data.items():
                setattr(user, field, value)
                update_fields.append(field)
            user.save(update_fields=update_fields)

            serializer = UserSerializer(instance=user)
            return Response(serializer.data)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        spending = get_object_or_404(User, id=id, owner=self.request.user)
        spending.delete()
        return Response({'detail': 'success'}, status=status.HTTP_204_NO_CONTENT)

class TopUsersView(APIView):

    def get(self, request):
        queryset = User.objects.all().annotate(total_score=Sum('scores__value')).order_by('-total_score')
        serializer = TopUserSerializer(queryset, many=True)
        return Response(serializer.data)


