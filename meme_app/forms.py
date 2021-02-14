from django import forms
from . models import Meme

# forms page to serialize the data from the db
class memesForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ('name', 'caption', 'url')

    name = forms.CharField(label='Meme Owner', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    caption= forms.CharField(label='Caption', widget=forms.TextInput(attrs={'placeholder': 'Give a catchy caption'}))
    url = forms.URLField(label='Meme URL', widget=forms.TextInput(attrs={'placeholder': 'Enter Image Link'}))
 