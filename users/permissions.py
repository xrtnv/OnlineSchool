from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """
    Проверка, что пользователь является модератором.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модераторы').exists()
