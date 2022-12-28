from rest_framework import filters
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)

from api.mixins import CreateListViewSet
from api.permissions import IsOwnerOrReadOnly
from api.serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer,
)
from posts.models import Post, Group


class PostViewSet(viewsets.ModelViewSet):
    """Получаем список всех постов.
    Получаем, редактируем или удаляем пост по id.
    """

    pagination_class = LimitOffsetPagination
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Получаем список всех групп.
    Получаем информацию о группе по id.
    """

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Получаем список всех комментариев поста.
    Получаем, редактируем или удаляем комментарий по id.
    """

    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CommentSerializer

    def get_post(self):
        """Возвращает пост"""
        return get_object_or_404(Post, pk=self.kwargs.get("post_id"))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(CreateListViewSet):
    """Получаем список подписок. Добавляем подписку."""

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
