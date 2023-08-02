from django import forms
from .models import Post, Comment

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
        
    
    