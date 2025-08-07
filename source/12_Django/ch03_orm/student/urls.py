from django.contrib import admin
from django.urls import path, register_converter
from . import views
from .converters import IdConverter
# "" -> student list 출력
# "/student" -> student list 출력
# "/student/get/2" -> id=2인 student 상세보기
# "/student/del/2" -> id=2인 student 삭제

app_name = "student"
register_converter(IdConverter, 'dddd')
urlpatterns = [
    path("", views.list, name='list'),
    path('get/<dddd:id>', views.get, name='get'),
    path('delete/<int:id>', views.delete, name='delete')
]