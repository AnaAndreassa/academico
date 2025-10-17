from django.contrib import admin
from .models import *

# Inline: CursoDisciplina dentro de Curso
class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]

# Inline: Matricula dentro de Pessoa
class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]

# Inline: Ocorrências dentro de Pessoa
class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1

# Adiciona as ocorrências também no admin de pessoa
PessoaAdmin.inlines.append(OcorrenciaInline)

# Se quiser usar Avaliações dentro de Curso:
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

CursoAdmin.inlines.append(AvaliacaoInline)

# Registro de modelos que não possuem customização
admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(InstituicaoEnsino)
admin.site.register(AreaSaber)
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(Frequencia)
admin.site.register(Turno)
admin.site.register(CursoDisciplina)
admin.site.register(AvaliacaoTipo)
