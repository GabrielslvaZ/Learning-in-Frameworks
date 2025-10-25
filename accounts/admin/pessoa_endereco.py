from django.contrib import admin
from accounts.models.pessoa_endereco import PessoaEndereco


@admin.register(PessoaEndereco)
class PessoaEnderecoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'endereco', 'ativo', 'data_inicio', 'data_fim')
    search_fields = ('pessoa__user__username', 'pessoa__cpf', 'endereco__logradouro__nome')
    list_filter = ('ativo', 'endereco__cidade', 'endereco__estado')