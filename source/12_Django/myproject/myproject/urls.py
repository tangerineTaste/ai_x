from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: redirect("blog:index")),
    path("blog/", include("blog.urls")),

]
