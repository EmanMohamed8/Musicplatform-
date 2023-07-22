from django.contrib.auth import get_user_model

User = get_user_model()


def test_valid_user_login(auth_client):
    user = User.objects.create_user(
        username='testuser', password='testpassword')

    client = auth_client()
    response = client.get('authentication/login/',
                          data={'user': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200
    assert 'token' in response.data


def test_invalid_user_login(auth_client):
    user = User.objects.create_user(
        username='testuser', password='testpassword')

    client = auth_client()

    response = client.get('authentication/login/',
                          data={'username': 'testuser', 'password': 'testpassword'})
    assert response == 401


def test_valid_user_registration(auth_client):

    response = auth_client.post(
        'authentication/register/', {'email': 'newuser@example.com', 'username': 'newuser', 'password1': 'newpassword1', 'password2': 'newpassword2'})

    assert response.status_code == 201


def test_invalid_user_registration(auth_client):
    response = auth_client.post(
        'authentication/register/', {'username': 'newuser', 'password1': 'newpassword1', 'password2': 'newpassword2'})

    assert response.status_code == 400

    assert 'email' in response.data


def test_invalid_user_registration(auth_client):
    response = auth_client.post(
        'authentication/register/', {'email': 'newuser@example.com', 'password1': 'newpassword1', 'password2': 'newpassword2'})

    assert response.status_code == 400

    assert 'username' in response.data


def test_invalid_user_registration(auth_client):
    response = auth_client.post(
        'authentication/register/', {'email': 'newuser@example.com', 'username': 'newuser',  'password2': 'newpassword2'})

    assert response.status_code == 400

    assert 'password1' in response.data


def test_invalid_user_registration(auth_client):
    response = auth_client.post(
        'authentication/register/', {'email': 'newuser@example.com', 'username': 'newuser', 'password1': 'newpassword1'})

    assert response.status_code == 400

    assert 'password2' in response.data
