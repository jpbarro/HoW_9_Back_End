from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'users', UserViewSet, basename='create_user')

urlpatterns = router.urls