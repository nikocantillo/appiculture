from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template




def create_mail(email, subject, template_path, context):

    template =  get_template(template_path)
    content = template.render(context)
    
    mail = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email='nikolacantillo@gmail.com',
        to=[
            email
        ],
        cc=[]
    )
    mail.attach_alternative(content, 'text/html')

    return mail