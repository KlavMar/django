
from django.urls import path
from app.blog.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',PostListView.as_view(),name="home_page"),
    path('image/',PostMediaView.as_view(),name="image_page"),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)