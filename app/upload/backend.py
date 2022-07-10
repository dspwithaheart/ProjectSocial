from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from upload.activeDirectory import active_directory_auth

class activeDirectoryAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
            login_valid = active_directory_auth(username,password) #(settings.ADMIN_LOGIN == username)
            print(login_valid)

            if login_valid:
                try:
                    print(username)
                    user = User(username, 'username@th-n.de', "password")
                except:
                    print("username: "+ username + " already exists")
                    return None
                return user
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None