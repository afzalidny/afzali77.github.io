from django import forms
from .models import Post_Kids, Comment

class EmailPostForm(forms.Form):
   name = forms.CharField(max_length=25)
   Email = forms.EmailField()
   to= forms.EmailField()
   subject = forms.CharField(required=False,
    widget=forms.Textarea)

class CommentForm(forms.ModelForm):
 class Meta:
  model = Comment
  fields = ('name', 'email', 'body')