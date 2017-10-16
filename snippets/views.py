from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly


# Snippets
class SnippetList(generics.ListCreateAPIView):
    """List all code snippets, or create a new snippet"""
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a code snippet."""
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


# Users
class UserList(generics.ListAPIView):
    """List all users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Retrieve a user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
