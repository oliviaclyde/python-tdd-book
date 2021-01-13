from django.test import TestCase

# Create your tests here.
class FakeTest(TestCase):
    def test_bath_maths(self):
        self.assertEqual(1+1, 3)