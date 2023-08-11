from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from artists.models import Artist
from albums.models import Album

User = get_user_model()


class EndpointsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser")
        self.artist = Artist.objects.create(user=self.user)

    def test_albums_list_endpoint(self):
        url = "/albums/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("results" in response.data)
        self.assertTrue("count" in response.data)
        self.assertTrue("next" in response.data)
        self.assertTrue("previous" in response.data)

    def test_create_album_unauthenticated(self):
        url = "/albums/"
        data = {
            "name": "Test Album",
            "release_datetime": "2023-07-20T00:00:00Z",
            "cost": 9.99,
            "approved": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_album_authenticated(self):
        self.client.force_login(self.user)
        url = "/albums/"
        data = {
            "name": "Test Album",
            "release_datetime": "2023-07-20T00:00:00Z",
            "cost": 9.99,
            "approved": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_custom_albums_endpoint(self):
        url = "/custom/albums/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# new task
