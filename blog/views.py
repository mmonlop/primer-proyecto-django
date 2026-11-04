from django.shortcuts import render
from .models import Post

# Create your views here.

def principal(request):
    posts = Post.objects.all()
    #importante, se usa mucho: 
    postManuel = Post.objects.filter(titulo__icontains='entrada')

    contexto = {
        "posts": posts,
    }
    return render(request,'blog/index.html',contexto)


def ji(request):
    return render(request,'blog/ji.html')

def detalle_post(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request,'blog/detallePost.html',{'post':post})

def autores_listado(request):
    posts = Post.objects.all()
    return render(request,'blog/autores.html',{'posts':posts})