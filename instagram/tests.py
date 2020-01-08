from django.test import TestCase
from .models import Profile,Image,Comment
# Create your tests here.

class ProfileTestClass(TestCase):

    #set up method
    def setUp(self):
        self.audrey= Profile(first_name = 'Audrey', last_name ='Mish', email ='mitchelaudrey@gmail.com')

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.audrey,Profile))