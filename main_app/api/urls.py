from rest_framework.routers import DefaultRouter

from main_app.api.viewsets import PostViewSet, UserViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
