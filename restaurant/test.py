from django.test import TestCase
from .models import menu
#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")