from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from django.contrib.auth.models import User
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuItemViewTests(TestCase):
    """
    Tests for the MenuItemView.
    This test case contains tests for the MenuItemView, which handles the API endpoints for menu items.
    Methods
    -------
    setUp():
        Sets up the test client, creates a test user, and a test menu item. Logs in the test user.
    test_get_menu_items():
        Tests the retrieval of menu items. It sends a GET request to the 'menu-list' endpoint and checks if the response status is 200 OK.
        It also verifies that the returned data matches the serialized data of all menu items in the database.
    test_create_menu_item():
        Tests the creation of a new menu item. It sends a POST request to the 'menu-list' endpoint with the data for a new menu item.
        It checks if the response status is 201 CREATED, verifies that the total count of menu items has increased by one, and confirms that
        the newly created menu item has the expected title.
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.menu_item = Menu.objects.create(title='Test Item', price=10.00, inventory=100)
        self.client.login(username='testuser', password='testpass')

    def test_get_menu_items(self):
        response = self.client.get(reverse('menu-list'))
        menu_items = Menu.objects.all().order_by('id')
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_create_menu_item(self):
        data = {'title': 'New Item', 'price': 15.00, 'inventory': 50}
        response = self.client.post(reverse('menu-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(Menu.objects.get(id=self.menu_item.id + 1).title, 'New Item')


