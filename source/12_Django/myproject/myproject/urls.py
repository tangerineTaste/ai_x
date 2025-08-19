from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: redirect("blog:index")),
    path("blog/", include("blog.urls")),
    path("book/", include("book.urls")),
    path("article/", include("article.urls")),
]
# 장고는 static은 자동 연결해주나, media는 url과 저장경로를 연결
from django.conf.urls.static import static
from . import settings
urlpatterns += static(settings.MEDIA_URL,
                      document_root = settings.MEDIA_ROOT) # BASE_DIR/_media/ 저장