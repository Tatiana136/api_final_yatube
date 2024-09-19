from rest_framework import serializers
from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Group.objects.all()
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    http_method_names = ['post', 'get']
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        # Автоматически устанавливает
        # значение поля user на текущего пользователя,
        # авторизованного в запросе.
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Follow

    def validate_following(self, value):
        if self.context['request'].user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        return value
