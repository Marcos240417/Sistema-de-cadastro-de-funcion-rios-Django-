from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Funcionario

class IndexTemplateView(TemplateView):
    template_name = "index.html" # Arquivo na raiz de templates

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista.html"
    context_object_name = "funcionarios"

class FuncionarioCreateView(CreateView):
    model = Funcionario
    template_name = "cria.html"
    fields = ['nome', 'sobrenome', 'cpf', 'tempo_de_servico', 'remuneracao']
    success_url = reverse_lazy("website:lista_funcionarios")

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    template_name = "cria.html"
    fields = ['nome', 'sobrenome', 'cpf', 'tempo_de_servico', 'remuneracao']
    success_url = reverse_lazy("website:lista_funcionarios")

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "excluir.html"
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")