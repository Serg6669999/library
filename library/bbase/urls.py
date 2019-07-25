from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_list, name='base_list'),
    path('post/<int:pk>/', views.book_list, name='book_list'),
    path('post/edit/', views.book_edit_list, name='book_edit_list'),

]