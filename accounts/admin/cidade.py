from django.contrib import admin
from django.db.models import Count
from accounts.models.cidade import Cidade

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado', 'total_logradouros')
    list_select_related = ('estado',) 
    search_fields = ('nome', 'estado__nome')  
    list_filter = ('estado',)
    list_per_page = 30 
    ordering = ('estado__nome', 'nome') 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('estado').annotate(
            logradouro_count=Count('logradouro', distinct=True)
        )

    def total_logradouros(self, obj):
        return getattr(obj, 'logradouro_count', 0)
    total_logradouros.admin_order_field = 'logradouro_count'
    total_logradouros.short_description = 'Total de Logradouros'