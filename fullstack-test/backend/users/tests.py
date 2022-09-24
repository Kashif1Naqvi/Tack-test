from django.test import TestCase
from users.models import User
from rest_framework.authentication import authenticate
# Create your tests here.


class RegisterViewTest(TestCase):
    def setUp(self):
        password = "testing123"
        username = "kashif"
        email = "kashif@gmail.com"
        first_name = "syed"
        last_name = "kashif"
        gender = "male"
        nationality = "pakistani"
        country = "pakistan"

        

        User.objects.create_user(password=password, username=username, email=email, first_name=first_name, last_name=last_name, gender=gender, nationality=nationality, country=country)



    def check_user_exist(self):
        
        u = User.objects.get(username="kashif")

        self.assertEqual(u.username, 'kashif')
        self.assertEqual(u.email, 'kashif@gmail.com')

