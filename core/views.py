from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DeleteView

from .models import Propriedade, ProprietarioPropriedade, Proprietario


class LoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/login'


class ProjectView(LoginRequiredMixin, TemplateView):
    template_name = 'project.html'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['propriedades'] = Propriedade.objects.all()
        context['proprietarios'] = ProprietarioPropriedade.objects.all()
        return context
