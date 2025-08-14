from django.shortcuts import render, redirect,   get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
# from .forms import BookForm, BookModelForm
from .forms import BookModelForm
from .models import Book

# 1. form없이 걍 2. form객체생성후(6장) 3. DjangoGenericView 이용 4. GenericView 상속(7장)
book_list = ListView.as_view(model=Book)

def book_new(request): # GET:template / POST:파라미터변수받아db에 save() ->book:list
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            book = Book(**form.cleaned_data)
            book.ip = request.META['REMOTE_ADDR']
            book.save()
            return redirect(book)
        else:
            return render(request, 'book/book_form.html', {'form':form})
    elif request.method == 'GET':
        form = BookModelForm()
        return render(request, 'book/book_form.html', {'form':form})

