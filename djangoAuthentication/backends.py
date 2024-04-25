from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
            if user.username[0].lower() in ['m', 'a'] and user.check_password(password):
                return user
            else:
                
                return None
        except User.DoesNotExist:
            print("User does not exist")
            return None
