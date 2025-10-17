from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoa/', PessoaView.as_view(), name='pessoa'),
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
    path('instituicaoensino/', InstituicaoEnsinoView.as_view(), name='instituicaoensino'),
    path('areasaber/', AreaSaberView.as_view(), name='areasaber'),
    path('curso/', CursoView.as_view(), name='curso'),
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),
    path('matricula/', MatriculaView.as_view(), name='matricula'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),
    path('turno/', TurnoView.as_view(), name='turno'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),
    path('cursodisciplina/', CursoDisciplinaView.as_view(), name='cursodisciplina'),
    path('avaliacaotipo/', AvaliacaoTipoView.as_view(), name='avaliacaotipo'),
    path('turma/', TurmaView.as_view(), name='turma'),
    path('delete/<int:id>/', DeletePessoaView.as_view(), name='delete'),
    path('editar/<int:id>/', EditarPessoaView.as_view(), name='editar'),
]
