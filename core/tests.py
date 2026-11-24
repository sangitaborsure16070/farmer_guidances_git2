from django.test import TestCase, Client
from django.urls import reverse
from core.weather_service import get_weather_data
from core.market_service import get_mandi_prices

class KisanMitraCoreTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_status(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_weather_page_status(self):
        response = self.client.get(reverse('core:weather'))
        self.assertEqual(response.status_code, 200)

    def test_market_prices_page_status(self):
        response = self.client.get(reverse('core:market_prices'))
        self.assertEqual(response.status_code, 200)

    def test_schemes_page_status(self):
        response = self.client.get(reverse('core:schemes'))
        self.assertEqual(response.status_code, 200)

    def test_crop_guidance_page_status(self):
        response = self.client.get(reverse('core:crop_guidance'))
        self.assertEqual(response.status_code, 200)

    def test_weather_fallback_structure(self):
        data = get_weather_data(city_name="InvalidCity12345")
        self.assertIn('temperature', data)
        self.assertIn('description', data)

    def test_mandi_fallback_structure(self):
        data = get_mandi_prices(state="Maharashtra")
        self.assertTrue(len(data) > 0)
        self.assertIn('commodity', data[0])