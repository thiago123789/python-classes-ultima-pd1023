from django import forms

from base.models import ContatoModel


class ContatoForm(forms.ModelForm):
    class Meta:
        model = ContatoModel
        fields = ['nome', 'email', 'mensagem']
