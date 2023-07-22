from django.contrib.auth import get_user_model

User = get_user_model()

# Test the behavior of the API view with permissions


def test_permission_classes(auth_client):
    user = User.objects.create_user(
        username='testuser', password='testpassword')

    client = auth_client()
    response = client.get(f'/users/{user.pk}/')
    assert response.status_code == 403

    restricted_client = auth_client(user=user)
    response = restricted_client.get(f'/users/{user.pk}/')
    assert response.status_code == 200

# Test the behavior of the API view with required fields


def test_missing_fields(auth_client):

    user = User.objects.create_user(
        username='testuser', password='testpassword')

    client = auth_client(user=user)

    response = client.post(f'/users/{user.pk}/', data={'username': 'testuser'})
    assert response.status_code == 400
    assert 'password' in response.data

    response = client.post(
        f'/users/{user.pk}/', data={'password': 'testpassword'})
    assert response.status_code == 400
    assert 'username' in response.data

    response = client.post(
        f'/users/{user.pk}/', data={})
    assert response.status_code == 400
    assert 'username' in response.data
    assert 'password' in response.data


# Test the behavior of the API view with expected fields

def test_expected_fields(auth_client):

    user = User.objects.create_user(
        username='testuser', password='testpassword')

    client = auth_client(user=user)
    response = client.get(f'/users/{user.pk}/')
    assert response.status_code == 200

    expected_data = {
        'id': user.pk,
        'username': user.username,
        'email': user.email,
    }
    assert response.json() == expected_data
