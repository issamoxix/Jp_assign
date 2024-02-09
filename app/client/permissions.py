from rest_framework.permissions import BasePermission
import jwt

class IsAuthenticatedCookie(BasePermission):
    """
    Allows access only to authenticated users with a valid JWT token in cookies.
    """

    def has_permission(self, request, view):
        token = request.COOKIES.get("jwt")
        if token:
            try:
                jwt.decode(token, "secret", algorithms=["HS256"])
                return True
            except jwt.ExpiredSignatureError:
                pass
        return False
