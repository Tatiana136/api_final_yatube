from rest_framework import permissions


class OnlyOwner(permissions.BasePermission):
    """Аутентификация/Внесение изменений."""

    def has_permission(self, request, view):
        # Запрет неавтоизированным пользователям
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
