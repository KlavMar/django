from django.contrib import admin
from app.blog.models import Post,Media,Category,Article,Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['post_name','date_create']
    list_filter = ['date_create']
    date_hierarchy = 'date_create'


class MediaAdmin(admin.ModelAdmin):
    pass 

class CategoryAdmin(admin.ModelAdmin):
    pass 

class ArticleAdmin(admin.ModelAdmin):
    list_display=['article_name','post_pk']

class CommentAdmin(admin.ModelAdmin):
    list_display=['author','post']
    list_filter=['author','post']

admin.site.register(Post,PostAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Media,MediaAdmin)
admin.site.register(Category,CategoryAdmin)