from django.contrib import admin
from app.blog.models import Post,Media,Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['post_name','date_create']
    list_filter = ['date_create']
    date_hierarchy = 'date_create'


class MediaAdmin(admin.ModelAdmin):
    pass 

class CategoryAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Post,PostAdmin)
admin.site.register(Media,MediaAdmin)
admin.site.register(Category,CategoryAdmin)