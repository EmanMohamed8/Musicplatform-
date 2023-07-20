from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django .http import Http404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()


class UserpkViews(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404

    def get(self, requset, pk):
        users = self.get_object(pk)
        serializer = UserSerializer(users)
        return Response(serializer.data)

    def put(self, requset, pk):
        users = self.get_object(pk)
        serializer = UserSerializer(users, data=requset.data)
        if serializer.is_valid():
            serializer.sava()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, requset, pk):
        users = self.get_object(pk)
        serializer = UserSerializer(users, data=requset.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
