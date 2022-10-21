"""User app URL Configuration."""
from rest_framework.routers import DefaultRouter

from app.user import views

router = DefaultRouter()
router.register("user", views.UserViewSet, basename="user")

urlpatterns = router.urls
