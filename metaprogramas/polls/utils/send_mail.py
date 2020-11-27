from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(path)


def send_user_mail(email, pk):
    subject = 'Titulo del correo'

    content = "Aquí tienes las respuestas de la encuesta. Gracias por participar"

    message = EmailMultiAlternatives(subject,  # Titulo
                                     content,
                                     settings.EMAIL_HOST_USER,  # Remitente
                                     [email])  # Destinatario

    message.attach("Respuestas", open(f'{path}/media/pdf/poll_{pk}.pdf', 'rb').read(), "application/pdf")
    message.send()
    print("Enviado")
