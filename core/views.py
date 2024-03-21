from django.shortcuts import render
from .forms import ContactForm
from slc_roboticas import settings
from django.template.loader import render_to_string
import os 
import smtplib
from email.message import EmailMessage
from django.views.generic import TemplateView 
from django.http import HttpResponse
from django.core.mail import send_mail

def enviar_email_assunto_mensagem(destinatario, assunto, mensagem):
    try:
        send_mail(
            subject=assunto,
            message=mensagem,
            from_email='igormarinhosilva@gmail.com',
            recipient_list=[destinatario],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return False




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
            
            resultado = enviar_email_assunto_mensagem(
            destinatario='igoormarinhosilva@gmail.com',
            assunto=f'Novo Contato - {nome}',
            mensagem=f'Nome: {nome},\nemail: {email},\ntelefone: {telefone},\nmenssagem: {menssagem}'
            )
            form = ContactForm()

            context = {'form':form,'formatarestilo':'margin-top: -10%;'}
            if resultado:
                    success_message = render_to_string('modulos/alerta.html', {'mensagem': 'Mensagem enviado com Sucesso.'})
                    
                    return HttpResponse(success_message)
                
            else:
                error_message = render_to_string('modulos/alerta.html', {'mensagem': 'Erro ao enviar o Mensagem.'})
                return HttpResponse(error_message, status=400)

            
        return render(request,'index.html',context)
class SobreView(TemplateView):
    
    template_name = "sobre.html"
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
