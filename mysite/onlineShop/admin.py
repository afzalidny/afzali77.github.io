from django.contrib import admin
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 list_display = ('title', 'slug', 'user', 'publish','img', 'visits','status')
 list_filter = ('status', 'created', 'publish', 'user')
 search_fields = ('title','')
 prepopulated_fields = {'slug': ('title',)}
 raw_id_fields = ('user',)
 date_hierarchy = 'publish'
 ordering = ('status', 'publish')