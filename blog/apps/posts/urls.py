from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    # path('posts/', posts, name='posts'), #En vista por funcion
    path('', views.PostListView.as_view(), name='posts'),
    path('posts/<int:id>/', views.PostDetailView.as_view(), name='post_individual'),
    path('post/categoria', views.CategoriaCreateView.as_view(), name='crear_categoria'),
    path('addPost', views.AddPost, name='addpost'),
    path('posts/<int:pk>/edit/', views.EditarPost, name='editarPost'),
    path('posts/<int:pk>/eliminar/', views.EliminarPost, name='borrarPost'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comment/add/<int:articulo_id>/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('categoria/<int:pk>/posts/', views.PostsPorCategoriaView.as_view(), name='posts_por_categoria'),
    path('categorias/',views.CategoriasListView.as_view(), name='categorias'),
    path('<int:pk>/like', views.like_post, name='like'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='borrar_categoria'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
