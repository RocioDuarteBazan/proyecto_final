from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Categoria
from .forms import PostForm, CommentForm
from django.views.generic import ListView, DetailView
from django.contrib import messages


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
          queryset = super().get_queryset()
          orden = self.request.GET.get('orden')
          if orden == 'reciente':
               queryset = queryset.order_by('-fecha')
          elif orden == 'antiguo':
               queryset = queryset.order_by('fecha')
          elif orden == 'alfabetico':
               queryset = queryset.order_by('titulo')
          return queryset
     
    def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['orden'] = self.request.GET.get('orden', 'reciente')
          return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

   
def EliminarPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST' and 'delete_articulo' in request.POST:
        post.delete()
        return render(request, 'posts/posts.html')


def AddPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) ##REQUEST FILE PARA LAS IMAGENES
        if form.is_valid():
            post = form.save(commit=False)
            # articulo.author = request.user #autor del articulo            
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    
    return render(request, 'posts/addPost.html', {'form': form})



def EditarPost(request, pk):
    posts = get_object_or_404(Post, pk=pk)

    # Solo el autor puede editar la noticia
    # if articulo.author != request.user:
    #     return HttpResponseForbidden("No tienes permisos para editar este artículo.")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return redirect('posts:post_individual', pk=pk)
    else:
        form = PostForm(instance=posts)

    context = {
        'form': form,
    }
    return render(request, 'posts/editarPost.html', context)


def add_comment(request, articulo_id):
    post = get_object_or_404(Post, id=articulo_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.user
        # creacion de comentario
        Comment.objects.create(articulo=post, author=author, text=text)
    return redirect('posts:post_individual', id=articulo_id)


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        if comment.author == request.user or request.user.is_staff:
            comment.delete()
            return redirect('posts:post_individual', id=comment.articulo.pk)

    # Confirmacion
    ctx = {
        "comentario": comment
    }
    return render(request, 'posts/comentarios/confirmar_eliminar.html', ctx)

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    #mensaje de error si no sos el autor
    if comment.author != request.user:
        messages.error(request, 'Usuario sin permisos para editar este comentario.')
        return redirect('posts:post_individual', id=comment.articulo.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('posts:post_individual', id=comment.articulo.pk)
    else:
        form = CommentForm(instance=comment)

    context = {
        'form': form,
        'comment': comment,
    }
    return render(request, 'posts/comentarios/editComentario.html', context)

class PostsPorCategoriaView(ListView):
     model = Post
     template_name = 'posts/posts_por_categoria.html'
     context_object_name = 'posts'

     def get_queryset(self):
          return Post.objects.filter(categoria_id=self.kwargs['pk'])
     