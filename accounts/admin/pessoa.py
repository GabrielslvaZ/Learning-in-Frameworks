from django.contrib import admin
from django.db.models import Prefetch
from accounts.models.pessoa import Pessoa
from accounts.models.pessoa_endereco import PessoaEndereco


class PessoaEnderecoInline(admin.TabularInline):  
    model = PessoaEndereco
    extra = 0
    autocomplete_fields = ['endereco'] 
    fields = ('endereco', 'data_inicio', 'data_fim', 'ativo')
    readonly_fields = ('data_inicio',)  


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'telefone', 'data_nascimento', 'endereco_atual_display')
    list_select_related = ('user',)
    list_per_page = 25
    search_fields = ('cpf', 'user__username', 'user__first_name', 'user__last_name')
    list_filter = ('data_nascimento',)
    inlines = [PessoaEnderecoInline]  

    def get_queryset(self, request):
        """Pré-carrega os endereços relacionados para evitar N+1 quando exibimos `endereco_atual`.

        Anexamos os registros de PessoaEndereco em `enderecos_prefetched` via `to_attr`, então o método
        `endereco_atual_display` pode acessar sem gerar queries adicionais.
        """
        qs = super().get_queryset(request)
        accessor = PessoaEndereco._meta.get_field('pessoa').remote_field.get_accessor_name()
        prefetch_qs = PessoaEndereco.objects.select_related('endereco')
        qs = qs.prefetch_related(Prefetch(accessor, queryset=prefetch_qs, to_attr='enderecos_prefetched'))
        return qs

    def endereco_atual_display(self, obj):
        """Retorna o endereço atual usando os dados pré-carregados (evita queries por linha)."""
        addrs = getattr(obj, 'enderecos_prefetched', None)
        if addrs is None:
           
            return obj.endereco_atual
        for rel in addrs:
            if getattr(rel, 'ativo', False):
                return getattr(rel, 'endereco', None)
        return None
    endereco_atual_display.short_description = 'Endereço atual'