#  Импортируйте в код всё необходимое
from rest_framework import viewsets, pagination, filters, mixins
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from posts.models import Post, Comment, Group
from .serializers import (
    PostSerializer, CommentSerializer,
    GroupSerializer, FollowSerializer
)

from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        return serializer.save(
            author=self.request.user
        )


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.get_post_obj().comments.all()

    def get_post_obj(self):
        return get_object_or_404(
            Post,
            pk=self.kwargs.get('post_pk')
        )

    def perform_create(self, serializer):
        return serializer.save(
            author=self.request.user,
            post=self.get_post_obj()
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.user.all()

    def perform_create(self, serializer):
        return serializer.save(
            user=self.request.user
        )
