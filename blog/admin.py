from django.contrib import admin
from .models import Category,Article,Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display=('name','article_num')

class ArticleAdmin(admin.ModelAdmin):
	list_display=('caption','category','createtime','hits','times','goods','bads')

class CommentAdmin(admin.ModelAdmin):
	list_display=('article','content','createtime','name','email')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)