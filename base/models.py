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


class Petshop(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100)
    rua = models.CharField(verbose_name='Rua', max_length=100)
    numero = models.CharField(verbose_name='Número', max_length=100)
    bairro = models.CharField(verbose_name='Bairro', max_length=50)
    dono1 = models.CharField(verbose_name='Dono1', max_length=60, blank=False)


class ReservaModel(models.Model):
    TAMANHO_OPCOES = (
        (0, 'Pequeno'),
        (1, 'Médio'),
        (2, 'Grande')
    )
    TURNO_OPCOES = (
        ('manha', 'Manhã'),
        ('tarde', 'Tarde')
    )
    nome = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    nome_pet = models.CharField(max_length=50, verbose_name='Nome do Pet')
    data = models.DateField(verbose_name='Data', help_text='dd/mm/yyyy')
    turno = models.CharField(verbose_name='Turno', max_length=10, choices=TURNO_OPCOES)
    tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES)
    obs = models.TextField(blank=True)
    petshop = models.ForeignKey('Petshop', related_name='reservas',
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)

    def __str__(self):
        return f'Tutor {self.nome}: {self.data} - {self.turno} para {self.nome_pet}'

    class Meta:
        verbose_name = 'Reserva de Banho'
        verbose_name_plural = 'Reservas de Banho'
