from django.test import TestCase
from ..models import Album, Artist
from ..serializers import AlbumSerializers
from django.contrib.auth import get_user_model

User = get_user_model()


class AlbumSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser")
        self.artist = Artist.objects.create(
            user=self.user, socialLink="https://example.com"
        )

    def test_album_serialization(self):
        album = Album.objects.create(
            id=1,
            artist=self.artist,
            name="Test Album",
            release_datetime="2023-07-20T00:00:00Z",
            cost=9.99,
            approved=True,
        )
        serializer = AlbumSerializers(album)

        expected_data = {
            "id": album.id,
            "artist": {
                "id": self.artist.id,
                "user": {
                    "id": self.user.id,
                    "user": self.user.username,
                    "socialLink": self.artist.socialLink,
                },
            },
            "name": "Test Album",
            "release_datetime": "2023-07-20T00:00:00Z",
            "cost": "9.99",
            "approved": True,
        }
        self.assertEqual(serializer.data, expected_data)

    def test_album_deserialization(self):
        album_data = {
            "artist": self.artist.id,
            "name": "Test Album",
            "release_datetime": "2023-07-20T00:00:00Z",
            "cost": 9.99,
            "approved": True,
        }
        serializer = AlbumSerializers(data=album_data)
        self.assertTrue(serializer.is_valid())
        album_instance = serializer.save()
        self.assertEqual(album_instance.name, "Test Album")
        self.assertEqual(album_instance.cost, 9.99)
        self.assertEqual(album_instance.artist, self.artist)

    # You can add more assertions here to check other fields

    def test_invalid_album_serialization(self):
        invalid_data = {
            "artist": self.artist.id,
            "name": "Test Album",
            "release_datetime": "2023-07-20T00:00:00Z",
            "cost": "invalid_cost",
            "approved": True,
        }
        serializer = AlbumSerializers(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("cost", serializer.errors)
