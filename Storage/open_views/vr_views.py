from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from Storage.open_utils.vr_utils import *
from Storage.forms import AddVerbalRiddles_post
from Storage.models import *

class Gallery_VerbalRiddles(DataMixin, ListView):
    model = VerbalRiddles
    template_name = "Storage/verbal_riddles/vr_gallery.html"
    context_object_name = 'verbal_riddles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Хранилище: Словесные загадки")
        context['addnew'] = ''
        if self.request.user.is_authenticated:
            context['addnew'] = 'Добавить'
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return VerbalRiddles.objects.filter(is_published = True)

class Show_VerbalRiddles(DataMixin, DetailView):
    model = VerbalRiddles
    template_name = "Storage/verbal_riddles/vr_show.html"
    pk_url_kwarg = "vrid"
    context_object_name = "vr"

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['Загадка'])
        return dict(list(context.items()) + list(c_def.items()))

class Add_VerbalRiddles(DataMixin, CreateView):
    form_class = AddVerbalRiddles_post
    template_name = 'Storage/verbal_riddles/vr_add.html'
    success_url = reverse_lazy('vr_add')
    raise_exception = True

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Создание")
        return dict(list(context.items()) + list(c_def.items()))


def main_page(requset):
    context = {}
    context['title'] = "О vr"

    return render(requset, 'Storage/main.html')
