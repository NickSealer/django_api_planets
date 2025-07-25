from celery import shared_task
from .mailers.new_planet_email import NewPlanetEmail

@shared_task(queue='emails')
def send_new_planet_email_task(data: dict):
  email = NewPlanetEmail(
    subject = data.get('subject'),
    to_emails = data.get('to_emails'),
    from_email = data.get('from_email'),
    template = data.get('template'),
    text_content = data.get('text_content'),
    context = data.get('context')
  )
  
  email.send_email()
