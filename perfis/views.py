from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil
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
  return render(request, 'perfil.html', {"perfil": perfil})

def convidar(request, perfil_id):
  convidar = Perfil.objects.get(id=perfil_id)
  logado = get_perfil_logado(request)
  logado.convidar(convidar)
  return redirect('index')

def aceitar(request, convite_id):
  convite = Convite.objects.get(id=convite_id)
  convite.aceitar()
  return redirect('index')

def get_perfil_logado(request):
  return Perfil.objects.get(id=5)