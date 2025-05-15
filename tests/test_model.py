from django.test import TestCase
from core.models import Student


class ItemModelTest(TestCase):
    def test_create_item(self):
        stu_obj = Student.objects.create(
            name="Test", roll_no=100, city="london")
        self.assertEqual(stu_obj.name, "Test")
