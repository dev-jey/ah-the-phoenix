import jwt
from rest_framework.views import status
from datetime import datetime, timedelta
from django.urls import reverse
from django.conf import settings
from rest_framework.test import APITestCase



class BaseTest(APITestCase):

    """Initiate all the data required in running other tests."""

    def setUp(self):
        """Define all variables required by other test cases."""
        self.login_url = reverse('authentication:user_login')
        self.signup_url = reverse('authentication:user_signup')
        self.user_url = reverse('authentication:user_url')
        self.password_reset_url = reverse('authentication:reset_password')
        self.user_data = {
            "user": {
                "username": "James",
                            "email": "wearethephoenix34@gmail.com",
                            "password": "jamesSavali1"
            }
        }

        self.user_data_duplicate_username = {
            "user": {
                "username": "James",
                            "email": "jame@gmail.com",
                            "password": "jamesSavali1"
            }
        }

        self.user_data_duplicate_email = {
            "user": {
                "username": "James2",
                            "email": "wearethephoenix34@gmail.com",
                            "password": "jamesSavali1"
            }
        }

        self.user_lacks_username = {
            "user": {
                "username": "",
                            "email": "wearethephoenix34@gmail.com",
                            "password": "jamesSavali1"
            }
        }

        self.user_lacks_email = {
            "user": {
                "username": "jamesS",
                            "email": "",
                            "password": "jamesSavali1"
            }
        }

        self.user_lacks_password = {
            "user": {
                "username": "james2",
                            "email": "wearethephoenix34@gmail.com",
                            "password": ""
            }
        }

        self.user_invalid_email = {
            "user": {
                "username": "james2",
                            "email": "jamgmail.com",
                            "password": "kenyanchiyetu"
            }
        }

        self.user_short_password = {
            "user": {
                "username": "james2",
                            "email": "wearethephoenix34@gmail.com",
                            "password": "kenya"
            }
        }

        self.user_wrong_password = {
            "user": {
                "username": "james2",
                            "email": "wearethephoenix34@gmail.com",
                            "password": "111"
            }
        }

        self.user_login_data = {
            "user": {
                "email": "wearethephoenix34@gmail.com",
                "password": "jamesSavali1"
            }
        }

        self.user_wrong_email_login = {
            "user": {
                "email": "jamaa@gmail.com",
                "password": "jamesSavali1"
            }
        }

        self.user_wrong_password_login = {
            "user": {
                "email": "wearethephoenix34@gmail.com",
                "password": "jamesSavali2"
            }
        }

        self.user_blank_email_login = {
            "user": {
                "email": "",
                "password": "jamesSavali1"
            }
        }

        self.user_blank_password_login = {
            "user": {
                "email": "wearethephoenix34@gmail.com",
                "password": ""
            }
        }

        self.username_nodigits = {
            "user": {
                "username": "23798731",
                "email": "james@gmail.com",
                "password": "jamesSavali1#"
                            
            }
        }

        self.short_username = {
            "user": {
                "username": "k",
                "email": "james@gmail.com",
                "password": "jamesSavali1#"

            }
        }

        self.password_lacks_specialchar = {
            "user": {
                "username": "kevinkibet",
                            "email": "kevin@andela.com",
                            "password": "kevinrules"
            }
        }

        self.non_superuser ={
            "user": {
                "username": "winston",
                "email": "winston@andela.com",
                "password": "Winston#67"
            }
        }


<<<<<<< HEAD
        self.email_forgot_password = {
                            "email": "wearethephoenix34@gmail.com"
        }

        self.empty_email_field = {
            "email":""
        }

        self.passwords={
            "password":"jamesSavali8@",
            "confirm_password":"jamesSavali8@"
        }

=======
>>>>>>> feat(authors haven):Display descriptive error messages when signing up
    def signup_a_user(self, user_details):
        """Invoke the server by sending a post request to the signup url."""
        return self.client.post(self.signup_url,
                                user_details,
                                format='json')

    def login_a_user(self, user_details):
        """Invoke the server by sending a post request to the login url."""
        return self.client.post(self.login_url,
                                user_details,
                                format='json')

    def send_reset_password_email(self, user_details):
        """Invoke the server by sending a post request to the password reset url."""
        return self.client.post(self.password_reset_url,
                                user_details,
                                format='json')

    @staticmethod
    def create_url():
        """Create a url with the token, to redirect the user to password update."""
        token = jwt.encode({"email": "wearethephoenix34@gmail.com",
                            "iat": datetime.now(),
                            "exp": datetime.utcnow() + timedelta(minutes=5)},
                            settings.SECRET_KEY,
                            algorithm='HS256').decode()
        reset_url = reverse("authentication:update_password",
             kwargs={"token": token})
        return reset_url
