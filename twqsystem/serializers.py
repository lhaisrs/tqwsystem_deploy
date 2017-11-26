from rest_framework import serializers
from .models import Relatorio, Formulario, ModeloFormulario, Constructo, Variavel, VariavelQuestao, Questao 
from .models import Resposta, Usuario, UsuarioFormulario, FuncaoUsuario, Equipe, EquipeUsuario, Projeto, Empresa, EmpresaProjeto


class RelatorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relatorio
        fields = ('Date_Created')

class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = ('IdModeloFormulario', 'Date_Expiration', 'Date_Send')

class ModeloFormularioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModeloFormulario
        fields = ('Nome', 'Descricao', 'Date_Created')

class ConstructoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constructo
        fields = ('Nome', 'IdModeloFormulario')

class VariavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variavel
        fields = ('Nome', 'IdConstructo')

class VariavelQuestaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariavelQuestao
        fields = ('IdFuncaoUsuario', 'IdQuestao', 'IdVariavel')

class QuestaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questao
        fields = ('Pergunta', 'Invertido', 'IdFormulario')

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = ('Valor', 'IdQuestao', 'IdUsuarioFormulario')

class UsuarioFormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioFormulario
        fields = ('Status_Respondido', 'IdUsuario', 'IdFormulario')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('Nome', 'UserName', 'Senha', 'Funcao')

class FuncaoUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FuncaoUsuario
        fields = ('Setor')

class EquipeUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipeUsuario
        fields = ('IdUsuario', 'IdEquipe')

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = ('IdProjeto')

class ProjetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projeto
        fields = ('Cliente', 'Status', 'Deadline', 'Nome')

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empresa
        fields = ('Nome')

class EmpresaProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaProjeto
        fields = ('IdEmpresa', 'IdProjeto')