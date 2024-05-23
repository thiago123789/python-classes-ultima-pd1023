import pytest
from pytest_django.asserts import assertTemplateUsed


def test_contato_view_should_return_template(client):
    response = client.get('/myapp/contato/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'contato.html')


@pytest.mark.django_db
def test_contato_view_set_contact_info(client):
    dados = {
        'nome': 'Maisa',
        'email': 'maisa@gmail.com',
        'mensagem': 'Quero uma reserva para meu cachorro bob'
    }
    response = client.post('/myapp/contato/', dados)
    assert response.status_code == 200
    assert 'Mensagem enviada com sucesso!' in str(response.content)


@pytest.mark.django_db
def test_contato_view_set_contact_info_error(client):
    dados = {
        'nome': 'Maisa',
        'email': 'maisa',
        'mensagem': 'Quero uma reserva para meu cachorro bob'
    }
    response = client.post('/myapp/contato/', dados)
    assert response.status_code == 200
    assert 'Mensagem enviada com sucesso!' not in str(response.content)

