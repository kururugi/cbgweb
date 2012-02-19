from django import forms

class ContactForm(forms.Form):
    ATTENTION_CHOICES = (
        ('webdev', "Web Development"),
        ('program', "Programming"),
        ('support', "Technical Support"),
        ('art', "Music and Visual Art"),
        ('all', "All"),
    )
    visitor_name = forms.CharField(label='Your name', max_length = 30)
    visitor_address = forms.EmailField(label='Your email')
    attention = forms.ChoiceField(choices=ATTENTION_CHOICES)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':'10', 'cols':'60'}))
