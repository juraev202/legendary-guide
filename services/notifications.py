def send_email_notification(email: str, subject: str, body: str):

    print(f"📧 Письмо отправлено на {email}: {subject}\n{body}")

def send_push_notification(user_id: int, title: str, message: str):

    print(f"📱 Push для {user_id}: {title} - {message}")
