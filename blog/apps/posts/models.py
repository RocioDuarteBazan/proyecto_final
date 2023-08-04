from pyexpat import model
from django.db import models
from django.utils import timezone
from django.conf import settings 
from django.urls import reverse
# Create your models here.

#Categoria:
class Categoria(models.Model):
    nombre =  models.CharField('Nombre', max_length=50, null=False)
    
    def __str__(self):
        return self.nombre
    
    def get_filterby_url(self):
        return f"{reverse('posts:posts')}?categoria_id={self.pk}"
    
class Post(models.Model):
    titulo = models.CharField(max_length=50,null=False)
    subtitulo = models.CharField(max_length=100,null =False, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoria')
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ('-publicado',)
        
    def __str__(self):
        return self.titulo
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()

    def get_absolute_url(self):
        return reverse('posts:post_individual', args=[self.pk])
        
    def get_editar_url(self):
        return reverse('posts:editarPost', args=[self.pk])
    
    def get_eliminar_url(self):
         return reverse('posts:borrarPost', args=[self.pk])
    
    def get_add_comment_url(self):
        return reverse('posts:add_comment', args=[self.pk])
    
 
        
class Comment(models.Model):
    articulo = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    