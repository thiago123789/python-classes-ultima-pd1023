from django.shortcuts import render

from base.forms import ContatoForm
from base.models import ExampleModel, ContatoModel


def inicio(request):
    return render(request, template_name='inicio.html')


def contato(request):
    sucesso = False
    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True
            form.save()
    contexto = {
        'nome': 'Maria',
        'telefone': '(99) 99999-9999',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', contexto)


# Create your views here.
def example_view(request):
    examples = ExampleModel.objects.all()
    return render(request,
                  template_name='example_template.html',
                  context={'examples': examples})
