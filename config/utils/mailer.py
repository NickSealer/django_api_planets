from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class Mailer():
  def __init__(self, subject: str, to_emails: list, from_email: str, template: str, text_content: str, context: dict):
    self.subject = subject
    self.to_emails = to_emails
    self.from_email = from_email
    self.template = template
    self.text_content = text_content
    self.context = context or {}
    
  def send_email(self):
    html_content = render_to_string(self.template, self.context)
    
    email = EmailMultiAlternatives(subject=self.subject, body=self.text_content, from_email=self.from_email, to=self.to_emails)
    email.attach_alternative(content=html_content, mimetype='text/html')
    email.send()
