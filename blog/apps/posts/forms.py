from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'texto', 'imagen', 'categoria']

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['text'] #campos de mi formulario
        exclude = ['author']
    
    