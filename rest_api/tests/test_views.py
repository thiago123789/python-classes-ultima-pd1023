import pytest
import datetime

from model_bakery import baker
from rest_framework.test import APIClient

from base.models import Petshop


@pytest.mark.django_db
def test_todos_petshop():
    client = APIClient()
    response = client.get('/api/petshop/')
    assert len(response.data['results']) == 0


@pytest.fixture()
def dados_reserva():
    petshop = baker.make(Petshop)
    return {
        'nome': 'Thiago',
        'email': 'thiago@email.com',
        'nome_pet': 'boby',
        'turno': 'manha',
        'tamanho': 0,
        'obs': '',
        'data': datetime.date.today(),
        'petshop': petshop
    }


@pytest.fixture()
def usuario():
    return baker.make('auth.User')


@pytest.mark.django_db
def test_criacao_reserva(usuario, dados_reserva):
    client = APIClient()
    client.force_authenticate(usuario)
    response = client.post('/api/reserva/', dados_reserva)
    assert response.status_code == 201

