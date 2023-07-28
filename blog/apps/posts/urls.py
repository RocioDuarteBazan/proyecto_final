from django.urls import path
# from .views import posts
from .views import PostListView, PostDetailView
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'apps.posts'

urlpatterns = [
    # path('posts/', posts, name='posts'), #En vista por funcion
    path('posts/',PostListView.as_view(), name='posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post_individual'),
    path('addArticulo', views.AddArticulo, name='addarticulo'),
    path('posts/<int:pk>/edit/', views.EditarArticulo, name='editarArticulo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    