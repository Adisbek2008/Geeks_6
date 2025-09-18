from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method == 'POST' and request.user.is_staff:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            if request.method in ('GET','PUT','PATCH','DELETE') or request.method in SAFE_METHODS:
                return True
            return False
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        return False
