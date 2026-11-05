from django.shortcuts import render
from .models import Post
from .models import Autor
from .models import Categoria

# Create your views here.

def principal(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    #importante, se usa mucho: 
    postManuel = Post.objects.filter(titulo__icontains='entrada')

    contexto = {
        "posts": posts,
        "categorias":categorias
    }
    return render(request,'blog/index.html',contexto)


def ji(request):
    return render(request,'blog/ji.html')

def detalle_post(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request,'blog/detallePost.html',{'post':post})

def autores_listado(request):
    autores = Autor.objects.all()
    return render(request,'blog/autores.html',{'autores':autores})

def entradas_autores(request,pk):
    autores = Post.objects.filter(autor=pk)
    return render(request,'blog/detalleAutores.html', {'autores':autores})

def categorias(request,pk):
    categoria = Categoria.objects.get(pk=pk)
    posts = Post.objects.filter(categoria=categoria)
    return render(request,'blog/categorias.html', {'posts':posts, 'categoria':categoria})