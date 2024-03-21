from django import forms
from core.models import Client

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        ''' remove any labels here if desired
        '''
        super(ContactForm, self).__init__(*args, **kwargs)
        # you can also remove labels of built-in model properties
        self.fields['full_name'].label = 'Nome/Empresa'
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].widget.attrs['id'] = 'name'
        self.fields['full_name'].widget.attrs['placeholder'] = 'Nome da Companhia'

       
        self.fields['email_addres'].label = 'E-mail'
        self.fields['email_addres'].widget.attrs['class'] = 'form-control'
        self.fields['email_addres'].widget.attrs['id'] = 'email'
        self.fields['email_addres'].widget.attrs['placeholder'] = 'exemplo@exemplo.com'
        # remove the label of a non-linked/calculated field (txt01 added at top of form)
       
        self.fields['phone_number'].label = 'Telefone'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['id'] = 'phone'
        self.fields['phone_number'].widget.attrs['mask'] = '(123) 456-7890'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Telefone'


        self.fields['message'].label = 'Menssagem'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['id'] = 'message'
        self.fields['message'].widget.attrs['placeholder'] = 'Escreva sua necessidade...'
        self.fields['message'].widget.attrs['style'] = 'height: 10rem'
