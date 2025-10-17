from django.db import models

# RF12 Gerenciar Cidades
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


# RF02 Gerenciar Ocupação de Pessoas
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


# RF01 Gerenciar Pessoas
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    pai = models.CharField(max_length=100, verbose_name="Nome do Pai", blank=True, null=True)
    mae = models.CharField(max_length=100, verbose_name="Nome da Mãe", blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade", blank=True, null=True)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, verbose_name="Ocupação", blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


# RF03 Gerenciar Instituição de Ensino
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituição")
    site = models.URLField(verbose_name="Site", blank=True, null=True)
    telefone = models.CharField(max_length=15, verbose_name="Telefone", blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"


# RF04 Gerenciar Áreas do Saber
class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área do Saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"


# RF05 Gerenciar Cursos
class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga Horária Total (em horas)")
    duracao_meses = models.IntegerField(verbose_name="Duração (meses)")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do Saber")
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de Ensino")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


# RF06 Gerenciar Turmas
class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


# RF07 Gerenciar Disciplinas
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do Saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


# RF08 Gerenciar Matrículas
class Matricula(models.Model):
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de Ensino")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_previsao_termino = models.DateField(verbose_name="Data de Previsão de Término")

    def __str__(self):
        return f"{self.pessoa.nome} - {self.curso.nome}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"


# RF09 Gerenciar Avaliações
class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    avaliacao_tipo = models.ForeignKey('AvaliacaoTipo', on_delete=models.CASCADE, verbose_name="Tipo de Avaliação")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


# RF10 Gerenciar Frequência
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de Faltas")

    def __str__(self):
        return f"{self.pessoa.nome} - {self.disciplina.nome}"

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"


# RF11 Gerenciar Turnos
class Turno(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do Turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"


# RF13 Gerenciar Ocorrências / Advertências
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso", blank=True, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina", blank=True, null=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa", blank=True, null=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"


# RF14 Gerenciar Disciplinas por Cursos
class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    periodo = models.CharField(max_length=50, verbose_name="Período", blank=True, null=True)

    def __str__(self):
        return f"{self.curso.nome} - {self.disciplina.nome}"

    class Meta:
        verbose_name = "Disciplina por Curso"
        verbose_name_plural = "Disciplinas por Cursos"


# RF15 Gerenciar Tipos de Avaliação
class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Tipo de Avaliação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"
