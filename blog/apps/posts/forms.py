from django import forms
from .models import Post, Comment, Categoria

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class CrearPostFrom(forms.ModelForm):
   class Meta:
       model = Post
       fields = '__all__'

class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
       model = Categoria
       fields = '__all__'



class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'texto', 'imagen', 'categoria']

class CommentForm(forms.ModelForm):
    text = forms.CharField(label='Escribe tu comentario', widget=forms.Textarea(attrs={
        "rows": 2,
        "class": "form-control",
        "placeholder": "Escribe tu comentario aquí...",
        "name": "text"
    }))
    class Meta:
        model = Comment
        fields = ['text']
        
    
