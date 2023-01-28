from rest_framework.permissions import BasePermission as DRFBasePermission

from gradebook.user import User


class BasePermission(DRFBasePermission):
    permission_name = None

    def has_permission(self, request, view=None):
        req = getattr(request, 'auth')

        if not isinstance(req, User):
            req = getattr(request, 'user')

        return bool(
            req and req.is_authenticated and req.group.name == self.permission_name
        )
