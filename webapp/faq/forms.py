from django import forms

class NewReply(forms.Form):
    text=forms.CharField(label='text',max_length=1000)
    author=forms.CharField(label='author',max_length=30)
    parent=forms.IntegerField(label='parent')

class Vote(forms.Form):
    id=forms.IntegerField(label='id')
    vote=forms.IntegerField(label='vote')