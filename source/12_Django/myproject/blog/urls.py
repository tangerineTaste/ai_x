from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path("",views.list, name="index"),
    path("<post_id>/", views.detail, name="detail"),
]
