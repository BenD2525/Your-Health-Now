from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views


class TestUrls(SimpleTestCase):
    ''' Tests for testing URL resolutions for each view. '''

    def test_home_url_is_resolved(self):
        ''' Tests home URL resolution '''
        url = reverse('HealthHub:home')
        self.assertEqual(resolve(url).func, views.home)
    
    def test_health_hub_url_is_resolved(self):
        ''' Tests health hub URL resolution '''
        url = reverse('HealthHub:health_hub')
        self.assertEqual(resolve(url).func, views.health_hub)

    def test_health_hub_tracker_url_is_resolved(self):
        ''' Tests health hub tracker URL resolution '''
        url = reverse('HealthHub:health_hub_tracker')
        self.assertEqual(resolve(url).func, views.health_hub_tracker)
    
    def test_health_hub_update_url_is_resolved(self):
        ''' Tests health hub update URL resolution '''
        url = reverse('HealthHub:health_hub_update')
        self.assertEqual(resolve(url).func.view_class, views.UpdateHealth)

    def test_health_hub_history_url_is_resolved(self):
        ''' Tests health hub history URL resolution '''
        url = reverse('HealthHub:health_hub_history')
        self.assertEqual(resolve(url).func, views.health_history)

    def test_health_hub_delete_url_is_resolved(self):
        ''' Tests health hub delete URL resolution '''
        id_x = int()
        url = reverse('HealthHub:health_hub_delete', args=[id_x])
        self.assertEqual(resolve(url).func.view_class, views.DeleteEntry)

    def test_health_hub_edit_url_is_resolved(self):
        ''' Tests health hub edit URL resolution '''
        id_x = int()
        url = reverse('HealthHub:health_hub_edit', args=[id_x])
        self.assertEqual(resolve(url).func.view_class, views.EditHealth)

    def test_article_detail_url_is_resolved(self):
        ''' Tests article detail URL resolution '''
        id_x = int()
        url = reverse('HealthHub:health_hub_article', args=[id_x])
        self.assertEqual(resolve(url).func, views.article_detail)