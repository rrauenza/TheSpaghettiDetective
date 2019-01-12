from django.db import models
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from app.models import Printer

class PrinterAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key, request=None):
        try:
            printer = Printer.objects.select_related('user').get(auth_token=key)
        except models.DoesNotExist:
            raise AuthenticationFailed({'error':'Invalid or Inactive Token', 'is_authenticated': False})

        return printer.user, printer