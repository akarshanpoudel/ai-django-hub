from rest_framework import permissions

class IsBelongToSameOrganization(permissions.BasePermission):
    """
    Allows access only to objects that belong to the user's organization.
    """
    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False
        return obj.organization == request.user.organization