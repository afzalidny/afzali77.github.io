from django.contrib import admin
from .models import  Post_Kids
from .models import Post_Kids, Comment
@admin.register( Post_Kids)
class PostAdmin(admin.ModelAdmin):
 list_display = ('title', 'slug', 'user', 'publish','img', 'visits','status')
 list_filter = ('status', 'created', 'publish', 'user')
 search_fields = ('title','')
 prepopulated_fields = {'slug': ('title',)}
 raw_id_fields = ('user',)
 date_hierarchy = 'publish'
 ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
 list_display = ('name', 'email', 'post', 'created', 'active')
 list_filter = ('active', 'created', 'updated')
 search_fields = ('name', 'email', 'body')