from apps.posts.models import Categoria

def blog_context(request):
    data = {
        'app_name': 'Eco Friendly',
        'categorias': Categoria.objects.all()
    }
    return data
