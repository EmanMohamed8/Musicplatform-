import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def auth_client():
    def get_auth_client(user=None):
        client = APIClient()
        if user is not None:
            client.force_authenticate(user=user)
        return client
    return get_auth_client
