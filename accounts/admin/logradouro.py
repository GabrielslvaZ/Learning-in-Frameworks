from django.contrib import admin
from accounts.models.logradouro import Logradouro

@admin.register(Logradouro)
class LogradouroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'tipo')
    search_fields = ('nome',)
    list_filter = ('cidade', 'tipo')