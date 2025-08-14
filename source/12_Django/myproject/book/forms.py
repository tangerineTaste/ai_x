from django import forms
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from .models import Book 

def save(self, commit=True):
    book = Book(**self.clean_data) # cleaned_data 입력데이터들을 검증 완료 데이터
    if commit:
        book.save()
    return book

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'sales']
