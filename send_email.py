import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(name, email, order):
    # E-Mail-Einstellungen
    sender_email = email
    receiver_email = "ziel_email@example.com"
    password = "dein_email_passwort"

    # Nachricht erstellen
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Neue Bestellung"

    body = f"""
    Name: {name}
    E-Mail: {email}
    Bestellung:
    {order}
    """

    message.attach(MIMEText(body, "plain"))

    # SMTP-Server initialisieren
    server = smtplib.SMTP("smtp.example.com", 587)
    server.starttls()
    server.login(sender_email, password)

    # E-Mail senden
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

# Beispielaufruf
send_email("Max Mustermann", "max@example.com", "3x Pizza Margherita, 2x Cola")
