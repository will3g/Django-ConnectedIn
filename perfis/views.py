from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil, Convite
from django.shortcuts import redirect

def index(request):
  return render(
    request,'index.html', 
    {
      'perfis' : Perfil.objects.all(),
      'logado' : get_perfil_logado(request)
    }
  )

def exibir(request, perfil_id):
  perfil = Perfil.objects.get(id=perfil_id)
  logado = get_perfil_logado(request)
  contato_existente = perfil in logado.contatos.all()
  return render(
    request, 'perfil.html', 
    {
      "perfil": perfil,
      "contato_existente": contato_existente
    }
  )

def convidar(request, perfil_id):
  convidar = Perfil.objects.get(id=perfil_id)
  logado = get_perfil_logado(request)
  logado.convidar(convidar)
  return redirect('index')

def aceitar(request, perfil_id):
  convite = Convite.objects.get(id=perfil_id)
  convite.aceitar()
  return redirect('index')

def get_perfil_logado(request):
  return Perfil.objects.get(id=5)