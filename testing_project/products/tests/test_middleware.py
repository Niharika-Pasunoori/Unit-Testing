from django.test import TestCase,override_settings
from django.urls import reverse


class MaintenanceModeTest(TestCase):

    @override_settings(MAINTENANCE_MODE=False)
    def test_maintenance_mode_off(self):
        """Test that the site works normally when MAINTENANCE_MODE is False"""
        # Simulate a request to the home page
        response=self.client.get(reverse('home'))

        # Check that the response is usccessful and normal content is returned 
        self.assertContains(response,'Welcome to our store', status_code=200)

    

    @override_settings(MAINTENANCE_MODE=True)
    def test_maintenance_mode_on(self):
        """Test that the site works normally when MAINTENANCE_MODE is False"""
        # Simulate a request to the home page
        response=self.client.get(reverse('home'))

        # Check that the response is sccessful and normal content is returned 
        self.assertContains(response,"Site is under maintenance", status_code=503)
