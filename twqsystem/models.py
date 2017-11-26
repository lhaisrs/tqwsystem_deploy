from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Relatorio(models.Model):
    Id = models.AutoField(primary_key=True)
    Date_Created = models.DateTimeField(default=timezone.now)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_specificrelatorio(cls, filter):
        return cls.objects.filter(filter)

    @classmethod
    def get_historic(cls):
        cls.objects.filter(Date_Created=timezone.now()).order_by('Data_Created')

    @classmethod
    def post_create(cls, relatorio):
        cls.objects.create(Data_Created=relatorio.Date_Created)

class Formulario(models.Model):
    """
    Formulario agora eh responsavel pela aplicacao do formulario somente, e agora ele precisa das questoes no modelo
    """
    Id = models.AutoField(primary_key=True)
    IdModeloFormulario = models.ForeignKey('ModeloFormulario',on_delete=models.PROTECT)
    Date_Expiration = models.DateTimeField(blank=True, null=True)
    Date_Send = models.DateTimeField(blank=True, null=True)

    @classmethod
    def get_formularios_timeout(cls, date):
        cls.objects.filter(Date_Expiration=date);
    
    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def isFormularioExpirado(self):
        return self.Date_Expiration < timezone.now()

class ModeloFormulario(models.Model):
    """
    Modelo da aplicacao do formulario, que contem as questoes a serem aplicadas nele
    """
    Id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=200)
    Descricao = models.TextField()
    Date_Created = models.DateTimeField(default=timezone.now)
    empresa = models.ForeignKey('Empresa',on_delete=models.PROTECT)

class Constructo(models.Model):
    Id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=200)
    IdModeloFormulario = models.ForeignKey('ModeloFormulario')

class Variavel(models.Model):
    Id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=200)
    IdConstructo = models.ForeignKey('Constructo',on_delete=models.PROTECT)
    IdFuncaoUsuario = models.ForeignKey('FuncaoUsuario',on_delete=models.PROTECT)

class VariavelQuestao(models.Model):
    Id = models.AutoField(primary_key=True)
    IdQuestao = models.ForeignKey('Questao',on_delete=models.PROTECT)
    IdVariavel = models.ForeignKey('Variavel',on_delete=models.PROTECT)

class Questao(models.Model):
    """
    """
    Id = models.AutoField(primary_key=True)
    Pergunta = models.TextField()
    Invertido = models.BooleanField()
    IdFormulario = models.ForeignKey('ModeloFormulario',on_delete=models.PROTECT)

    @classmethod
    def get_questoes_form(cls, form):
        return cls.objects.filter(IdFormulario=form)

class Resposta(models.Model):
    Id = models.AutoField(primary_key=True)
    Valor = models.IntegerField()
    IdQuestao = models.ForeignKey('Questao',on_delete=models.CASCADE)
    IdUsuarioFormulario = models.ForeignKey('UsuarioFormulario',on_delete=models.PROTECT)

class UsuarioFormulario(models.Model):
    Id = models.AutoField(primary_key=True)
    Status_Respondido = models.BooleanField()
    IdUsuario = models.ForeignKey('Usuario',on_delete=models.PROTECT)
    IdFormulario = models.ForeignKey('Formulario')

class Usuario(models.Model):
    Id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=200)
    UserName = models.CharField(max_length=200)
    Senha = models.CharField(max_length=100)
    Funcao = models.ForeignKey('FuncaoUsuario')

    @classmethod
    def get_user(self):
        self.objects.filter(Id=self.Id)

class FuncaoUsuario(models.Model):
    Id = models.AutoField(primary_key=True)
    Setor = models.CharField(max_length=200)

class EquipeUsuario(models.Model):
    Id = models.AutoField(primary_key=True)
    IdUsuario = models.ForeignKey('Usuario')
    IdEquipe = models.ForeignKey('Equipe')

class Equipe(models.Model):
    Id = models.AutoField(primary_key=True)
    IdProjeto = models.ForeignKey('Projeto',on_delete=models.SET_NULL,blank=True, null=True)

class Projeto(models.Model):
    Id = models.AutoField(primary_key=True)
    Cliente = models.CharField(max_length=200)
    Status = models.BooleanField()
    Deadline = models.DateTimeField(blank=True, null=True)
    Nome = models.CharField(max_length=200)

class Empresa(models.Model):
    Id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=200)

class EmpresaProjeto(models.Model):
    Id = models.AutoField(primary_key=True)
    IdEmpresa = models.ForeignKey('Empresa')
    IdProjeto = models.ForeignKey('Projeto')