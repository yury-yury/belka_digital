from django.contrib.auth import login
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import User
from users.serializers import UserCreateSerializer, LoginSerializer


class UserCreateView(CreateAPIView):
    """
    The UserCreateView class inherits from the CreateAPIView class from the rest_framework.generics module and is
    a class-based view for processing requests with POST methods at the address '/users/signup'.
    """
    model = User
    serializer_class = UserCreateSerializer
    permission_classes: list = [AllowAny]


class LoginView(CreateAPIView):
    """
    The LoginView class inherits from the CreateAPIView class from the rest_framework.generics module and is
    a class-based view for processing requests with POST methods at the address '/users/login'.
    """
    serializer_class = LoginSerializer
    permission_classes: list = [AllowAny]

    def post(self, request, *args, **kwargs) -> Response:
        """
        The post function overrides the method of the parent class. Accepts the request object and any positional
        and named arguments as parameters. If the method is called, it checks and serializes the received data
        and calls the login method for the User class object. Returns serialized object data in JSON format.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(serializer.data)
