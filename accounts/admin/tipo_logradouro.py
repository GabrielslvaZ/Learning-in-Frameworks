from django.contrib import admin
from accounts.models.tipo_logradouro import TipoLogradouro

@admin.register(TipoLogradouro)
class TipoLogradouroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)