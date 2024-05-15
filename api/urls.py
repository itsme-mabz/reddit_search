from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RedditPostViewSet

router = DefaultRouter()
router.register(r'api', RedditPostViewSet, basename='api-view')

urlpatterns = [
    path('', include(router.urls)),
]
