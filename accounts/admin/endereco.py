from django.contrib import admin
from accounts.models.endereco import Endereco

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'cidade', 'estado', 'cep')
    list_filter = ('estado', 'cidade')
    search_fields = ('logradouro', 'numero', 'cidade', 'estado')