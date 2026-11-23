from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated and request.user.is_staff:
            return True
        return False
