from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django import forms

from .models import User, Book


class NameForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name_user',)

class BookForm(forms.ModelForm):

     class Meta:
         model = Book
         fields = ('title_book',)









class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)