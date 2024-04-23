import logging
from .models import Post
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import PostSerializer, UserSerializer
from rest_framework.decorators import api_view, action
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from django.http import Http404

#VIEWSET POST
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)
        try:
            instance = self.get_object()
            title = instance.title
            self.perform_destroy(instance)
            return Response({"message": f"Post '{title}' deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except Http404:
            logger.warning("Post não encontrado.")
            return Response({"message": "Post não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error("Erro ao deletar o post: %s", str(e))
            return Response({"message": "Erro ao deletar o post."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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