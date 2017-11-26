from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'formulario', views.get_formulario, name='formulario'),
    url(r'relatorio', views.get_relatorio, name='relatorio'),
    url(r'relatorios', views.get_relatorios, name='relatorios'),
    url(r'^relatorio/equipe/(?P<equipe_id>\d+)/(?P<formulario_id>\d+)', views.get_relatorio_equipe, name='equipe_relatorio'),
    url(r'^relatorio/historico', views.get_historic_relatorio, name='historico'),
    url(r'^relatorio/analise', views.get_analise_relatorio, name='analise'),
    url(r'^empresa/(?P<empresaid>\d+)/create_form/$', views.create_form, name='create_form'),
    url(r'^formulario/(?P<formularioid>\d+)/create_questions/$', views.create_questions, name='create_questions'),
    url(r'^usuario/(?P<usuarioid>\d+)/formulario/(?P<formularioid>\d+)/responder/$', views.responder_formulario, name='responder_formulario')
]