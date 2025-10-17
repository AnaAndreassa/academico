from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from .forms import PessoaForm
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'index.html', {'pessoas': pessoas})

# Gerenciar Pessoas
class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

# Gerenciar Ocupações
class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

# Gerenciar Instituições de Ensino
class InstituicaoEnsinoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicaoensino.html', {'instituicoes': instituicoes})

# Gerenciar Áreas do Saber
class AreaSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = AreaSaber.objects.all()
        return render(request, 'areasaber.html', {'areas': areas})

# Gerenciar Cursos
class CursoView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

# Gerenciar Disciplinas
class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})

# Gerenciar Matrículas
class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})

# Gerenciar Avaliações
class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})

# Gerenciar Frequências
class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})

# Gerenciar Turnos
class TurnoView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turno.objects.all()
        return render(request, 'turno.html', {'turnos': turnos})

# Gerenciar Cidades
class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

# Gerenciar Ocorrências
class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})

# Gerenciar Disciplinas por Cursos
class CursoDisciplinaView(View):
    def get(self, request, *args, **kwargs):
        curso_disciplinas = CursoDisciplina.objects.all()
        return render(request, 'cursodisciplina.html', {'curso_disciplinas': curso_disciplinas})

# Gerenciar Tipos de Avaliação
class AvaliacaoTipoView(View):
    def get(self, request, *args, **kwargs):
        tipos_avaliacao = AvaliacaoTipo.objects.all()
        return render(request, 'avaliacaotipo.html', {'tipos_avaliacao': tipos_avaliacao})

class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})

class DeletePessoaView(View):
    def get(self, request, id, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, id=id)
        pessoa.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('index')

class EditarPessoaView(View):
    template_name = 'editar_pessoa.html'
    def get(self, request, id, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, id=id)
        form = PessoaForm(instance=pessoa)
        return render(request, self.template_name, {'pessoa': pessoa,'form': form})
    def post(self, request, id, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, id=id)

        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            messages.success(request, 'As edições foram salvas com sucesso.')
            return redirect('editar', id=id) # Redirecionar de volta para a página de edição
        else:
            messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
            return render(request, self.template_name, {'pessoa': pessoa,'form': form})
