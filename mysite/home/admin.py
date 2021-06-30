from django.contrib import admin
from .models import Main
@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
 list_display = ('title', 'slug', 'auther',)
 list_filter = ( 'auther',)
 search_fields = ('title',)
 prepopulated_fields = {'slug': ('title',)}
 raw_id_fields = ('auther',)
 