from django import forms


class ContactForm(forms.Form):
    """ Create form for contact page """

    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control border-black rounded-0 mb-3',
            'placeholder': 'Email',
        })
    )
    message = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'rows': 5,
            'class': 'form-control border-black rounded-0 mb-3',
            'placeholder': 'Type your message here...',
        })
    )
