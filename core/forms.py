from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    
    name = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail")
    message = forms.CharField(label="Mensagem", widget=forms.Textarea)

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = "Nome: {0}\nEmail: {1}\nMensagem: {2}".format(name, email, message)
        send_mail(
            subject='Contato do MeuBaz',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL]
        )

    """
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['rows'] = '4'
    """

        # self.fields['name'] acessa o campo
        #<input type="text" name="name" maxlength="100" required="" id="id_name">
        # .widget.attrs[''] = '' pode criar argumentos dentro do campo