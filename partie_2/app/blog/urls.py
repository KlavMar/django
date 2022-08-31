
from django.urls import path
from app.blog.views import *
from django.conf import settings
from django.conf.urls.static import static
from app.blog import views
urlpatterns = [
    path('',PostListView.as_view(),name="home_page"),
    path('post/<int:pk>/',views.ArticleView,name='post_page'),
    path('post/<str:tag>/',views.PostCategories,name="post_categories"),
    path('image/',PostMediaView.as_view(),name="image_page"),
    
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)