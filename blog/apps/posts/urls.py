from django.urls import path
# from .views import posts
from .views import PostListView, PostDetailView, PostsPorCategoriaView
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    # path('posts/', posts, name='posts'), #En vista por funcion
    path('', PostListView.as_view(), name='posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post_individual'),
    path('addPost', views.AddPost, name='addpost'),
    path('posts/<int:pk>/edit/', views.EditarPost, name='editarPost'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comment/add/<int:articulo_id>/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('categoria/<int:pk>/posts/',PostsPorCategoriaView.as_view(), name='posts_por_categoria'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
