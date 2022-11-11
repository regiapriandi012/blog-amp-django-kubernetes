from .models import Comment
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class CommentFormAmp(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)