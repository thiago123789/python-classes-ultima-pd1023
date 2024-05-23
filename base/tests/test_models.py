from datetime import date

import pytest
from model_bakery import baker

from base.models import Petshop, ReservaModel


def test_config():
    assert 1 == 1


@pytest.mark.django_db
def test_qtd_reservas_should_return():
    petshop = baker.make(Petshop)
    qtd = 5
    baker.make(ReservaModel,
               qtd, petshop=petshop)

    assert petshop.qtd_reservas() == qtd


@pytest.fixture
def reserva():
    date_reserva = date(2024, 5, 16)
    reserva = baker.make(ReservaModel, data=date_reserva, nome='Maria', turno='manha', nome_pet='Bob')
    return reserva


@pytest.mark.django_db
def test_str_reserva_returns_formatted_string(reserva):
    assert str(reserva) == 'Tutor Maria: 2024-05-16 - manha para Bob'
