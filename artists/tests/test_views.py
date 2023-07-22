from django.contrib.auth import get_user_model
from rest_framework import status
from ..models import Artist

User = get_user_model()

# Test the behavior of the API view with permissions


def test_permission_classes(auth_client):
    artist = Artist.objects.create(
        stageName='Test Artist', socialLink='http://example.com')

    unauthenticated_client = auth_client()

    response = unauthenticated_client.get(f'/artists/{artist.pk}/')
    assert response.status_code == status.HTTP_200_OK

    response = unauthenticated_client.put(f'/artists/{artist.pk}/')
    assert response.status_code == status.HTTP_403_FORBIDDEN

    authenticated_client = auth_client(user=artist)

    response = authenticated_client.get(f'/artists/{artist.pk}/')
    assert response.status_code == status.HTTP_200_OK

    response = authenticated_client.put(f'/artists/{artist.pk}/')
    assert response.status_code == status.HTTP_200_OK


# Test the behavior of the API view with required fields


def test_missing_fields(auth_client):
    artist = Artist.objects.create(
        stageName='Test Artist', socialLink='http://example.com')

    authenticated_client = auth_client(user=artist)

    # Make a POST request to the ArtistList view with a missing field
    response = authenticated_client.post('/artists/', data={})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'stageName' in response.data.keys()

    # Make a PUT request to the ArtistPk view with a missing field
    artist = Artist.objects.create(
        stageName='Test Artist', socialLink='http://example.com')
    response = authenticated_client.put(
        f'/artists/{artist.pk}/', data={})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'stageName' in response.data.keys()


# Test the behavior of the API view with expected fields
def test_expected_fields(auth_client):

    artist = Artist.objects.create(
        stageName='Test Artist', socialLink='http://example.com')

    client = auth_client()

    response = client.get(f'/artists/{artist.pk}/')

    assert response.status_code == status.HTTP_200_OK

    expected_data = {
        'id': artist.pk,
        'stageName': 'Test Artist',
        'socialLink': 'http://example.com',
    }
    assert response.json() == expected_data
