from django.test import TestCase
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer

# Create your tests here.
class MenuViewTest(TestCase):
    def setUp(self):
        # Create test Menu instances here
        menu1 = MenuItem.objects.create(title="Steak", price=300, inventory=6)
        menu2 = MenuItem.objects.create(title="Grilled Chicken", price=150, inventory=20)

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get('/api/menu-items')
        serializer = MenuItemSerializer(MenuItem.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)