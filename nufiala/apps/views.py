# from django.shortcuts import render

# #from django.contrib.auth.models import User

# from datetime import datetime

# from .utils import send_email_with_html_body
# from django.core.mail import send_mail

# # Create your views here.

# # def index(request, *args, **kwargs):
# #     context = {

# #     }

# #     return render(request, 'index.html', context)


# def create_view(request, *args, **kwargs):

#      ctx = {}

#      if request.method == 'POST':
#          email = request.POST.get('email')


#          subjet = "Test Email"
#          template = 'email.html'
#          context = {
#              'date':datetime.today().date,
#              'email':email
#          }

#          receivers  = [email]

#          has_send = send_email_with_html_body(
#              subjet = subjet,
#              receivers = receivers,
#              template =  template,
#              context=context
#              )
        
#          print(has_send)
        
#          if has_send:
#              ctx =  {"msg":"Mail envoyée avec Succès"}
        
#          else:
#              ctx = {"msg":"Envoie de mail echoué !!!"}
    
#      return render(request,'index.html', ctx)



# def create_view(request, *args, **kwargs):
#     if request.method == 'POST':
#         nom = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         subject = request.POST.get('subject')
        
#         sujet = f"Message de {nom} ({email})"
#         message_email = f"De : {email}\n\n{message}"
#         destinataires = ['esseyjoseph17@gmail.com']
        
#         has_send = send_mail(sujet, message_email, email, destinataires)

#         if has_send:
#              ctx =  {"msg":"Mail envoyée avec Succès"}
        
#         else:
#             ctx = {"msg":"Envoie de mail echoué !!!"}
            

#     else:
#         return render(request, 'index.html', ctx)


from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

def create_view(request, *args, **kwargs):
    ctx = {}
    if request.method == 'POST':
        nom = request.POST.get('name')
        email_expediteur = request.POST.get('email')
        sujet = request.POST.get('subject')
        message = request.POST.get('message')

        sujet = f"Message de {nom} ({email_expediteur}) sujet : {sujet}"

        # Envoyer l'e-mail
        has_send = send_mail(
            sujet,
            message,
            email_expediteur,
            ['dessiigo@gmail.com'],
            fail_silently=False,
        )

        if has_send:
            ctx =  {"msg":"Mail envoyée avec Succès"}
        
        else:
            ctx = {"msg":"Envoie de mail echoué !!!"}
            
    
    return render(request, 'index.html',ctx)