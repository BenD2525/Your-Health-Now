from django.test import RequestFactory, SimpleTestCase
from django.urls import reverse, resolve
from . import views
from . import urls

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('HealthHub:home')
        self.assertEqual(resolve(url).func, views.home)
    
    def test_health_hub_url_is_resolved(self):
        url = reverse('HealthHub:health_hub')
        self.assertEqual(resolve(url).func, views.health_hub)

    def test_health_hub_tracker_url_is_resolved(self):
        url = reverse('HealthHub:health_hub_tracker')
        self.assertEqual(resolve(url).func, views.health_hub_tracker)
    
    def test_health_hub_update_url_is_resolved(self):
        url = reverse('HealthHub:health_hub_update')
        self.assertEqual(resolve(url).func, views.UpdateHealth())

    def test_health_hub_history_url_is_resolved(self):
        url = reverse('HealthHub:health_hub_history')
        self.assertEqual(resolve(url).func, views.health_history)

    def test_article_detail_url_is_resolved(self):
        id_x = int()
        url = reverse('HealthHub:health_hub_article', args=[id_x])
        self.assertEqual(resolve(url).func, views.article_detail)