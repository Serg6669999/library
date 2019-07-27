from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django import forms
from .models import user


class NameForm(forms.ModelForm):

    class Meta:
        model = user
        fields = ('name_user',)
    #your_name = forms.CharField(label='Добавить пользователя', max_length=100)

class BookForm(forms.ModelForm):

   class Meta:
       model = user
       fields = ('name_book',)

    #book_name = forms.CharField(label='Добавить книгу', max_length=100)






class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)