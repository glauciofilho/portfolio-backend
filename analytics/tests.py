from django.test import TestCase, Client
from unittest.mock import patch

class AnalyticsEndpointTest(TestCase):
    def setUp(self):
        self.client = Client()

    @patch("analytics.views.get_overview")
    def test_analytics_overview(self, mock_get_overview):
        mock_get_overview.return_value = {
            "users": 100,
            "events": 200,
            "page_views": 300
        }
        response = self.client.get("/analytics/overview/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"users": 100, "events": 200, "page_views": 300})

    @patch("analytics.views.get_overview")
    def test_analytics_overview_error(self, mock_get_overview):
        mock_get_overview.side_effect = Exception("API Error")
        response = self.client.get("/analytics/overview/")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"error": "API Error"})

    @patch("analytics.views.get_countries")
    def test_analytics_countries(self, mock_get_countries):
        mock_get_countries.return_value = [{"country": "Brazil", "total": 50}]
        response = self.client.get("/analytics/countries/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"country": "Brazil", "total": 50}])

    @patch("analytics.views.get_project_events")
    def test_analytics_projects(self, mock_get_project_events):
        mock_get_project_events.return_value = [{"project_id": "1", "total": 10}]
        response = self.client.get("/analytics/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"project_id": "1", "total": 10}])
