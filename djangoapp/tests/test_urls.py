from django.test import TestCase
from django.urls import reverse


class UrlsTest(TestCase):
    print("UrlsTest start...\n")

    def test_measurements_url_exists_at_desired_location(self):
        response = self.client.get("/measurements/")
        self.assertEqual(response.status_code, 200)

    def test_measurements_url_accessible_by_name(self):
        response = self.client.get(reverse('measurements-list'))
        self.assertEqual(response.status_code, 200)

    def test_api_url_exists_at_desired_location(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)

    def test_api_temperature_url_exists_at_desired_location(self):
        response_temperarure = self.client.get("/api/temperature/")
        self.assertEqual(response_temperarure.status_code, 200)

    def test_api_pressure_url_exists_at_desired_location(self):
        response_pressure = self.client.get("/api/pressure/")
        self.assertEqual(response_pressure.status_code, 200)

    def test_api_humidity_url_exists_at_desired_location(self):
        response_humidity = self.client.get("/api/humidity/")
        self.assertEqual(response_humidity.status_code, 200)

    def test_admin_api_url_exists_at_desired_location(self):
        response = self.client.get("/admin/", follow=True)
        self.assertEqual(response.status_code, 200)

    print("UrlsTest end...\n")
