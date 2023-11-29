from django.test import TestCase
from .models import Menu

#Menu Testcase
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price =45, inventory= 70)
        self.assertEqual(item, "IceCream : 45")
