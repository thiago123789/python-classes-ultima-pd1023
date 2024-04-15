from django.db import models


# Create your models here.
class ExampleModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Formulário de Exemplo'
        ordering = ['name']


class ContatoModel(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False, verbose_name='Lido', blank=True)

    def __str__(self):
        return f'{self.pk} {self.nome} [{self.email}]'

    class Meta:
        verbose_name = 'Forlumário de Contato'
        ordering = ['-created_at']

