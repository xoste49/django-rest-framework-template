from http import HTTPStatus

import pytest
from django.test import Client
from server.settings.components.healthcheck import HEALTHCHECK_SECRET_TOKEN


@pytest.mark.django_db()
def test_health_check(client: Client) -> None:
    """This test ensures that health check is accessible."""
    response = client.get(f'/health/{HEALTHCHECK_SECRET_TOKEN}/')

    assert response.status_code == HTTPStatus.OK