from django.test import TestCase
from base.models import User

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        User.objects.create(name_user='Trol')

    def test_name_user_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name_user').verbose_name
        self.assertEquals(field_label, 'name_user')



    def test_object_name_user(self):
        user = User.objects.get(id=1)
        expected_object_name = '%s, %s' % (user.name_user)
        self.assertEquals(expected_object_name, str(author))

