from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Categoria
from .forms import PostForm, CommentForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib import messages
from django.views.generic import CreateView
from .forms import ComentarioForm, CrearPostFrom, NuevaCategoriaForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

#Vista basada en funciones
# def posts(request):
#     posts = Post.objects.all()
#     return render(request, 'posts.html', {'posts' : posts})


#Vista basada en clases
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'



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






class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CrearPostFrom
    template_name = 'posts/crear_post.html'
    success_url = reverse_lazy('apps.posts:posts')

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'posts/crear_categoria.html'

    def get_success_url(self):
        messages.success(self.request, '¡categoria creada con exito!')
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('apps.posts:post-create')
        

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = CrearPostFrom
    template_name = 'posts/modificar_post.html'
    success_url = reverse_lazy('apps.posts.posts')

class PostdeleteView(DeleteView):
    model = Post
    template_name ='post/eliminar_post.html'
    success_url = reverse_lazy('apps.posts:posts')