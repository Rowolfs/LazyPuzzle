from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from Storage.open_utils.vr_utils import *
from Storage.forms import AddThemes_post
from Storage.models import *

class Gallery_Themes(DataMixin, ListView):
    model = Themes
    template_name = "Storage/themes/th_gallery.html"
    context_object_name = 'themes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Хранилище: Темы")
        context['addnew'] = ''
        if self.request.user.is_authenticated:
            context['addnew'] = 'Добавить'
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return VerbalRiddles.objects.filter(is_published = True)

class Add_Themes(DataMixin, CreateView):
    form_class = AddThemes_post
    template_name = 'Storage/themes/th_add.html'
    success_url = reverse_lazy('th_add')
    raise_exception = True

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Создание")
        return dict(list(context.items()) + list(c_def.items()))


def main_page(requset):
    context = {}
    context['title'] = "О th"

    return render(requset, 'Storage/main.html')
