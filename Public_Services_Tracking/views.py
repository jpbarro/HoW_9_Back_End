from .models import Post
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer, UserSerializer
from rest_framework.decorators import api_view, action
from django.contrib.auth.models import User

#VIEWSET POST
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#VIEWSET CRIAR USUARIO
class UserViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def create_user(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"user_id": user.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)