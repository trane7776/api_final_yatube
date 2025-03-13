from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

appname = 'api'

router = SimpleRouter()
router.register('v1/posts', PostViewSet, basename='posts')
router.register('v1/groups', GroupViewSet, basename='groups')
router.register('v1/follow', FollowViewSet, basename='follow')
router.register(r'v1/posts/(?P<post_pk>\d+)/comments', CommentViewSet,
                basename='comments')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
