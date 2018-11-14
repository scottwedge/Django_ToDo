from django.test import TestCase

# Create your tests here.

# methods need to start wiht test_
class TestDjango(TestCase):

    def test_this_thing_on(self):
        self.assertEqual(1, 1)