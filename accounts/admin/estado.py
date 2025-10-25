from django.contrib import admin
from django.db.models import Count, Prefetch
from .models import Estado
from accounts.models.cidade import Cidade

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sigla', 'total_cidades', 'total_enderecos')
    list_per_page = 25
    search_fields = ('nome', 'sigla')
    ordering = ('nome',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related(
            Prefetch(
                'cidade_set',
                queryset=Cidade.objects.only('id', 'estado_id').annotate(
                    endereco_count=Count('endereco', distinct=True)
                ),
                to_attr='cidades_prefetched'
            )
        ).annotate(
            cidade_count=Count('cidade', distinct=True),
            endereco_total=Count('cidade__endereco', distinct=True)
        )

    def total_cidades(self, obj):
        return getattr(obj, 'cidade_count', 0)
    total_cidades.admin_order_field = 'cidade_count'
    total_cidades.short_description = 'Total de Cidades'

    def total_enderecos(self, obj):
        return getattr(obj, 'endereco_total', 0)
    total_enderecos.admin_order_field = 'endereco_total'
    total_enderecos.short_description = 'Total de Endereços'