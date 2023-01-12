from django.shortcuts import render
from .forms import ContactForm
from slc_roboticas import settings
# Create your views here.
import os 
import smtplib
from email.message import EmailMessage
from django.views.generic import TemplateView 

def enviar_email(nome,email,telefone,menssagem):
        msg = EmailMessage()
        msg['subject'] = f'{nome} Solicita um Orçamento.'
        msg['From'] = 'contato@solucoesroboticas.com.br'
        msg['To'] = settings.EMAIL_ADDRESS
        msg.set_content(f'Requerente: {nome}.\nEmail: {email}.\nTelefone: {telefone}.\nMenssagem: {menssagem}.')

        with smtplib.SMTP_SSL('mail.solucoesroboticas.com.br',465) as smtp:
            smtp.login('contato@solucoesroboticas.com.br',settings.EMAIL_PASSWORD)
            smtp.send_message(msg)
class HomeView(TemplateView):
    
    template_name = "index.html"
    
    

    def get_context_data(self, **kwargs):
        kwargs['mostrar'] = 'd-none'
        kwargs['form'] = ContactForm()
        
        return super().get_context_data(**kwargs)
    
   
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            nome = form['full_name'].value()
            email = form['email_addres'].value()
            telefone = form['phone_number'].value()
            menssagem = form['message'].value()
            form = ContactForm()
            enviar_email(nome,email,telefone,menssagem)

            return render(request,'index.html',{'form':form,'mostrar':'','formatarestilo':'margin-top: -10%;'})