from django.contrib import admin
from django.contrib import messages

# Register your models here.
from base.models import ContatoModel, ReservaModel
from base.models import ExampleModel
from base.models import Petshop

@admin.action(description='Marcar como lido')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(read=True)
    modeladmin.message_user(request, f'Objetos marcados como lido', messages.SUCCESS)


@admin.register(ContatoModel)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['pk','nome', 'email', 'created_at', 'read']
    search_fields = ['nome', 'email']
    list_filter = ['created_at', 'read']
    actions = [marcar_como_lido]


@admin.register(Petshop)
class PetshopAdmin(admin.ModelAdmin):
    list_display = ['pk', 'nome']
    search_fields = ['nome']


@admin.register(ReservaModel)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['pk']





@admin.register(ExampleModel)
class ExampleAdmin(admin.ModelAdmin):
    pass

