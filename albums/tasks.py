from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_congratulatory_email(artist_name, artist_email, album_name):
    # Prepare the congratulatory email content
    print("new task")
    email_subject = f"Congratulations, {artist_name}!"
    email_message = (
        f"Dear {artist_name},\n\n"
        f"Your new album '{album_name}' has been released. "
        f"Congratulations on this exciting release!\n\n"
        f"Sincerely,\nYour Record Label"
    )
    send_mail(
        subject=email_subject,
        message=email_message,
        # from_email="eman.mohamed3061@gmail.com",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[artist_email],
        fail_silently=True,
    )
    return f"Congratulatory email sent to {artist_name}"
