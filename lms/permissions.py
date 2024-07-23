from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Право доступа, позволяющее объекты редактировать и удалять только их владельцам.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
