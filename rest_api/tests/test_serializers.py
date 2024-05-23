import datetime

import pytest
from model_bakery import baker

from base.models import Petshop
from rest_api.serializers import ReservaModelSerializer


@pytest.fixture()
def dados_agendamneto_invalido():
    ontem = datetime.date.today() - datetime.timedelta(days=1)
    petshop =  baker.make(Petshop)
    return {
        'nome': 'Thiago',
        'email': 'thiago@email.com',
        'nome_pet': 'boby',
        'turno': 'manha',
        'tamanho': 0,
        'obs': '',
        'data': ontem,
        'petshop': petshop.pk
    }


@pytest.mark.django_db
def test_dados_agendamento_incorreto(dados_agendamneto_invalido):
    serializer = ReservaModelSerializer(data=dados_agendamneto_invalido)
    assert not serializer.is_valid()