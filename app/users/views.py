from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
import jwt, datetime


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201, data={"message": "Registration successful"})


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=401, data={"message": "Invalid email"})

        if not user.check_password(password):
            return Response(status=401, data={"message": "Invalid password"})

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")

        response = Response(status=200)
        response.set_cookie(key="jwt", value=token, httponly=True, samesite="Strict")

        response.data = {"message": "Login successful"}

        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            return Response(status=401, data={"message": "Unauthorized"})

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return Response(status=401, data={"message": "Unauthorized"})

        user = User.objects.filter(id=payload["id"]).first()
        serializer = UserSerializer(user)

        return Response(
            status=200, data={"message": "success", "user": serializer.data}
        )


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "success"}
        return response
