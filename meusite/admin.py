from django.contrib import admin
from .models import Post, Pessoa, Endereco


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
	list_display = ('rua', 'numero', 'bairro', 'cidade', 'estado', 'cep')
	search_fields = ('rua', 'bairro', 'cidade', 'estado', 'cep')


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
	def get_full_name(self, obj):
		return obj.usuario.get_full_name() or obj.usuario.username
	get_full_name.short_description = 'Nome'

	list_display = ('get_full_name', 'usuario', 'email', 'cpf', 'telefone')
	search_fields = ('email', 'cpf', 'rg', 'usuario__username', 'usuario__first_name', 'usuario__last_name')
	list_filter = ('data_nascimento',)
	raw_id_fields = ('usuario', 'endereco')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'data_criacao')
	search_fields = ('titulo',)





