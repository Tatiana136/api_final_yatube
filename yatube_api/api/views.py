from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly)
from posts.models import Post, Group, Comment, Follow
from api.serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer)
from .permissions import OnlyOwner


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return (IsAuthenticatedOrReadOnly(),)
        else:
            return (OnlyOwner(),)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs.get('post_id'))

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return (IsAuthenticatedOrReadOnly(),)
        return (OnlyOwner(),)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    http_method_names = ['post', 'get']
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        following = serializer.validated_data.get('following')
        serializer.save(user=self.request.user, following=following)
