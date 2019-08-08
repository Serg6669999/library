from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from .models import User, Book
from .forms import NameForm, BookForm

def base_list(request):

    users = User.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            #user = form.cleaned_data['your_name']
            #print(user['your_name'])
            #Post.objects.create(name_user = user)
            #Post.objects.create(name_user=NameForm.your_name())
            return HttpResponseRedirect('/')
    else:
        form = NameForm()
    return render(request, 'base/base_list.html', {'users': users, 'form': form})

def book_list(request, pk):

    user = get_object_or_404(User, pk=pk)
    #user = User.objects.filter(name_user='Lord')[0]
    books = Book.objects.filter(User=user)
    books_all = Book.objects.all()

    print(books_all)
    print(user)
    print(books)

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            title_book = form.save(commit=False)
            title_book.User = user
            title_book.save()
            return redirect('book_list', pk=pk)
    else:
        form = BookForm()
    return render(request, 'base/book_list.html',  {'user': user, 'form': form})

def book_edit_list(request,pk):

    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book_edit = form.save(commit=False)
            book_edit.save()
            return redirect('book_list', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'base/book_edit_list.html', {'form': form})