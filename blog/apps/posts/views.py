from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

#Vista basada en funciones
# def posts(request):
#     posts = Post.objects.all()
#     return render(request, 'posts.html', {'posts' : posts})


#Vista basada en clases
class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()
    

def EliminarArticulo(request, pk):
    articulo = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST' and 'delete_articulo' in request.POST:
        articulo.delete()
        return render(request, 'posts/posts.html')


def AddArticulo(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) ##REQUEST FILE PARA LAS IMAGENES
        if form.is_valid():
            articulo = form.save(commit=False)
            # articulo.author = request.user #autor del articulo            
            articulo.save()
            return redirect('index')
    else:
        form = PostForm()
    
    return render(request, 'posts/add.Articulo.html', {'form': form})



def EditarArticulo(request, pk):
    articulo = get_object_or_404(Post, pk=pk)

    # Solo el autor puede editar la noticia
    # if articulo.author != request.user:
    #     return HttpResponseForbidden("No tienes permisos para editar este artículo.")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('app.posts:post_individual', pk=pk)
    else:
        form = PostForm(instance=articulo)

    context = {
        'form': form,
    }
    return render(request, 'posts/editarArticulo.html', context)