#Gerais
import json
import datetime

#Gerais do Django: HTTP
from django.shortcuts import render
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.mail import send_mail, BadHeaderError 
from django.utils.timezone import datetime
from django.utils.html import escape
from django.core import serializers
from django.utils import timezone

#Models
from .models import Resposta
from .models import EquipeUsuario
from .models import Equipe
from .models import Relatorio
from .models import Formulario, UsuarioFormulario
from .models import ModeloFormulario, Questao, Variavel, VariavelQuestao, Constructo
from .models import Usuario, FuncaoUsuario, Empresa

#Serializers
from .serializers import RelatorioSerializer, RelatorioSerializer, FormularioSerializer, FuncaoUsuarioSerializer
from .serializers import ConstructoSerializer, EmpresaProjetoSerializer, EmpresaSerializer, EquipeSerializer, EquipeUsuarioSerializer
from .serializers import ModeloFormularioSerializer, ProjetoSerializer, QuestaoSerializer, UsuarioFormularioSerializer
from .serializers import UsuarioSerializer, VariavelQuestaoSerializer, VariavelSerializer


#RESTAPI
from rest_framework.decorators import api_view
from rest_framework import viewsets

#Importando os métodos de Análise
from Analise.entidades.formulario import Formulario as FormularioAnalise
from Analise.entidades.constructo import Constructo as ConstructoAnalise
from Analise.entidades.variavel import Variavel as VariavelAnalise
from Analise.entidades.questao import Questao as QuestaoAnalise



# Create your views here.

class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.get_all()
    serializer_class = RelatorioSerializer

# def get_relatorio_equipe(request, equipe_id, formulario_id):
#     equipes_usuarios = EquipeUsuario.objects.all().filter(IdEquipe = equipe_id)
    
#     formulariosAnalise = []

#     formulario = Formulario.objects.all().filter(Id = formulario_id).first()
#     modelo_formulario = ModeloFormulario.objects.all().filter(Id = formulario.IdModeloFormulario).first()
#     constructos = Constructo.objects.all.filter(IdModeloFormulario = modelo_formulario.Id)
    
#     for equipe_usuario in equipes_usuarios :
#         usuario = Usuario.objects.all().filter(Id = equipe_usuario.IdUsuario).first()
#         form_nome = modelo_formulario.Nome
#         form_descricao = modelo_formulario.Descricao
#         user_form = UsuarioFormulario.objects.all().filter(IdUsuario = usuario.Id, IdFormulario = formulario.Id).first()

#         form_constructos = []
#         for constructo in constructos:
            
#             form_constr_nome = constructo.Nome
#             form_constr_variaveis = []
#             variaveis = Variavel.objects.all().filter(IdConstructo = constructo.Id)
#             for variavel in variaveis:
#                 var_nome = variavel.Nome

#                 var_quests = []
#                 questoes = VariavelQuestao.objects.all().filter(IdVariavel = variavel.Id)
#                 for questao in questoes:
#                     pergunta = questao.Pergunta
#                     invertido = questao.Invertido
#                     resposta = Resposta.objects.all().filter(IdQuestao = questao.Id, IdUsuarioFormulario = user_form.Id).first()

#                     quest = QuestaoAnalise(pergunta,invertido,resposta.valor)
#                     var_quests.append(quest)
                
#                 vari = VariavelAnalise(var_nome,var_quests)
#                 form_constr_variaveis.append(vari)
            
#             constr = ConstructoAnalise(form_constr_nome,form_constr_variaveis)
#             form_constructos.append(constr)
#         form = FormularioAnalise(form_nome,form_descricao,usuario.Nome,form_constructos)
#         formulariosAnalise.append(form)

#     analisador = Analisador()
#     resultados = analisador.gerarRelatorio(formulariosAnalise)

#     return JsonResponse(serializers.serialize('json', resultados))

# def get_formulario(request,formulario_id, usuario_id):
#     return JsonResponse({})
  
# #Get_Relatorios: Obter todos os relatórios
# @api_view(['GET'])
# def get_relatorios(request):
#     relatorios = Relatorio.get_all()
#     rels = []
#     for relatorio in relatorios:
#         rels.append({relatorio.Id : relatorio.Date_Created})
        
#     response = JsonResponse({'relatorios': rels}, safe=True)
#     return response

# @api_view(['GET'])
# def get_relatorio(request, relatorioId):
#     return JsonResponse({"message": relatorioId}, safe=True)

# @api_view(['GET'])
# def get_formulario(request):
#    forms = Formulario.objects.all()
#    response = []
#    for form in forms:
#        response.append({form.Id:form.IdModeloFormulario})

#    return JsonResponse({'forms': response})

#     #return JsonResponse({'Formulario': {'Id':formulario.Id}})

# #Get_SpecificRelatorio: Obter relatórios através da análise
# def get_analise_relatorio(request, filter):
#     analise = Relatorio.get_specificrelatorio(filter)
#     response = JsonResponse({'analise': analise}, safe=True)
#     return HttpResponse(response)
    

# #Get_HistoricRelatorio: Obter histórico dos relatórios
# def get_historic_relatorio(request):
#     historic = Relatorio.get_historic()
#     response = JsonResponse({'historico': historic}, safe=True)
#     return HttpResponse(response)
    

# #Post_CreateRelatorio: Criar relatório
# def post_create_relatorio(request, relatorio):
#     if request.method == 'POST':
#         Relatorio.post_create(relatorio)
#         return HttpResponseRedirect()    

# #Get_ExportPDF: Exportar relatório para PDF
# def export_pdf(request, filter):
#     # Create the HttpResponse object with the appropriate PDF headers.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'

#     buffer = BytesIO()

#     # Create the PDF object, using the BytesIO object as its "file."
#     p = canvas.Canvas(buffer)

#     #Gerando os dados do relatório baseado na análise necessária
#     dados = Relatorio.get_specificrelatorio(filter)

#     #Colocar aqui os dados que serão gerados dos relatórios após analise 
#     p.drawString(100, 100, dados)

#     # Close the PDF object cleanly.
#     p.showPage()
#     p.save()

#     # Get the value of the BytesIO buffer and write it to the response.
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response

# #Send_Relatorio_Email: Enviar relatorio por email
# def send_relatorio_email(request, useremail):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, useremail) #Colocar o email do usuário que será enviado
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('') #Redirecionar baseado no sucesso do envio
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')

# #Get_User: Obter usuário
# def get_user(request):
#     user = Usuario.get_user()
#     response = JsonResponse({'usuario': user}, safe=True)
#     return HttpResponse(response)

# #Get_Formulario_Timeout: Obter os formulários em tempo de expiração (menos de 24 horas)
# def get_formulario_timeout():
#     date_from = datetime.datetime.now() - datetime.timedelta(days=1)
#     formularios = Formulario.get_formularios_timeout(date_from)
#     response = JsonResponse({'formularios': formularios}, safe=True)
#     return HttpResponse(response)

# def responder_formulario(request, usuarioid, formularioid):
#     if request.method == 'GET':
#         try:
#             uf = UsuarioFormulario.objects.get(IdUsuario=usuarioid,pk=formularioid)
#         except UsuarioFormulario.DoesNotExist:
#             return HttpResponse('No user or form exist', status=404)

#         if uf.IdFormulario.isFormularioExpirado():
#             return HttpResponse('Form expired', status=400)
#         else:
#             modeloform = uf.IdFormulario.IdModeloFormulario
#             constructors = Constructo.objects.filter(IdModeloFormulario=modeloform)
#             variables = Variavel.objects.filter(IdConstructo=constructors, IdFuncaoUsuario=uf.IdUsuario.Funcao)
#             variablequestions = VariavelQuestao.objects.filter(IdVariavel__in=variables).values('IdQuestao').distinct()
#             questions = Questao.objects.filter(pk__in=variablequestions)
#             data = serializers.serialize('json', questions)
#             response = JsonResponse({'questions':data,'expirationDate':uf.IdFormulario.Date_Expiration,'title':modeloform.Nome, 'description':modeloform.Descricao}, safe=True)
#             return HttpResponse(response, content_type="application/json")
        
# def send_form_to_company(request):
#     if request.method == 'POST':
#         companyId = request.POST.get('companyId','')
#         empresaProjetos = EmpresaProjeto.objects.filter(id = companyId)
#         equipes = Equipe.objects.filter(IdProjeto__in = empresaProjetos.values('IdProjeto'))
#         equipeUsuarios = EquipeUsuario.objects.filter(IdEquipe__in = equipes.values('id'))
#         usuarios = Usuario.objects.filter(id=equipeUsuarios.values('IdUsuario'))

#         for email in usuarios.values('UserName'):
#             try:
#                 send_mail('Novo formulario','message','email que ta enviando',email)
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#         return HttpResponse('OK')

# def create_form(request, empresaid):
#     if request.method == 'POST':
#         data = request.POST['data']
#         data = json.loads(data)
        
#         title = data.get('form-title', False)
#         description = data.get('form-description', False)
#         company = data.get('form-company', False)
#         constructors = data['form-constructors']
#         if title and description and company and constructors != []:
#             form = ModeloFormulario()
#             form.Nome = title
#             form.Descricao = description
#             try:
#                 form.empresa = Empresa.objects.get(pk=company)
#             except Empresa.DoesNotExist:
#                 return HttpResponse("Company must exist",status=404)
#             form.save()

#             for constructor in constructors:
#                 name = constructor.get('name', False)
#                 variables = constructor['variables']
#                 if name and variables != []:
#                     c = Constructo()
#                     c.Nome = name
#                     c.IdModeloFormulario = form
#                     c.save()

#                     for variable in variables:
#                         v = Variavel()
#                         v.Nome = variable.get('name')
#                         v.IdConstructo = c
#                         try:
#                             v.IdFuncaoUsuario = FuncaoUsuario.objects.get(pk=variable['role'])
#                             v.save()
#                         except FuncaoUsuario.DoesNotExist:
#                             return HttpResponse('Role must exist',status=404)
#                 else:
#                     return HttpResponse("Required fields must exist",status=400)
#         else:
#             return HttpResponse("Required fields must exist",status=400)

#         return HttpResponse(status=200)
#     else:
#         data = serializers.serialize('json', FuncaoUsuario.objects.all())
#         return HttpResponse(data, content_type="application/json")

# def create_questions(request, formularioid):
#     if request.method == 'POST':
#         data = request.POST['data']
#         data = json.loads(data)

#         try:
#             form = ModeloFormulario.objects.get(Id=data['formId'])
#         except ModeloFormulario.DoesNotExist:
#             return HttpResponse("Form doesn't exist",status=404)

#         if data['questions'] != []:
#             for question in data['questions']:
#                 title = question.get('title', False)
#                 inverted = question.get('inverted', False)
#                 variables = question.get('variables', None)
#                 if title and  inverted != None and variables != []:
#                     q = Questao()
#                     q.Pergunta = title                    
#                     q.Invertido = inverted
#                     q.IdFormulario = form
#                     q.save()

#                     for variable in variables:
#                         try:
#                             v = Variavel.objects.get(Id=variable)
#                         except Variavel.DoesNotExist:
#                             return HttpResponse("Varible doesn't exist",status=404)

#                         vq = VariavelQuestao()
#                         vq.IdQuestao = q
#                         vq.IdVariavel = v
#                         vq.save()
#                 else:
#                     return HttpResponse('Required fields must exist',status=400)
#         else:
#             return HttpResponse('No question was sent',status=400)

#         return HttpResponse(status=200)
#     else:
#         form = ModeloFormulario.objects.get(pk=formularioid)
#         constructors = Constructo.objects.filter(IdModeloFormulario=form)
#         variables = Variavel.objects.filter(IdConstructo=constructors)

#         data = serializers.serialize('json', variables)
#         return HttpResponse(data, content_type="application/json")

        
