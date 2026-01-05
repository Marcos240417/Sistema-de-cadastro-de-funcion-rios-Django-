from django.urls import path
from .views import (
    IndexTemplateView, FuncionarioListView, FuncionarioCreateView,
    FuncionarioUpdateView, FuncionarioDeleteView
)

app_name = 'website'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),
    path('funcionario/<int:pk>/', FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),
    path('funcionario/excluir/<int:pk>/', FuncionarioDeleteView.as_view(), name='deleta_funcionario'),
]