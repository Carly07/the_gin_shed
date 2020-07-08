from django import forms


class ContactForm(forms.Form):
    """ Create form for contact page """

    first_name = forms.CharField(
        required=True,
        label='First Name',
        widget=forms.Textarea(attrs={
            'rows': 1,
            'class': 'form-control border-black rounded-0 mb-3',
        })
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        widget=forms.Textarea(attrs={
            'rows': 1,
            'class': 'form-control border-black rounded-0 mb-3',
        })
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.Textarea(attrs={
            'rows': 1,
            'class': 'form-control border-black rounded-0 mb-3',
        })
    )
    message = forms.CharField(
        required=True,
        label='Message',
        widget=forms.Textarea(attrs={
            'rows': 8,
            'class': 'form-control border-black rounded-0 mb-3',
        })
    )
