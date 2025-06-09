from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

def require_token(view_func):
    def wrapped_view(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        if token != settings.API_TOKEN_SECRETO:
            return Response({"detail": "Token inválido ou ausente."}, status=status.HTTP_403_FORBIDDEN)
        return view_func(self, request, *args, **kwargs)
    return wrapped_view