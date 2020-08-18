from django.contrib import admin
from BlogApp.models import Article
from BlogApp.models import User,Comment
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','id')

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex','c_time')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'at_article','pub_time','words')

admin.site.register(Article, ArticleAdmin)
admin.site.register(User)
admin.site.register(Comment,CommentAdmin)
