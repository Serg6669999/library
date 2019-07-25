from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import NameForm, BookForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def base_list(request):
    posts = Post.objects.all()
    print(Post.name_user)
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
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'bbase/base_list.html', {'posts': posts, 'form': form})



def book_list(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post)
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('book_list', pk=pk)
    else:
        form = BookForm()
    return render(request, 'bbase/book_list.html',  {'post': post, 'form': form})

def book_edit_list(request,pk):

    return render(request, 'bbase/book_edit_list.html', )
