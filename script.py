import smtplib 
from email.mime.text import MIMEText # mimetext is a class that represent the text of the email.
from email.mime.multipart import MIMEMultipart # mimemultipart is a class that represent the email message itself
import os

def send_mail(workflow_name, repo_name, workflow_run_id):
    # email details
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    #email message
    subject = f"Workflow {workflow_name} failed for repo {repo_name}"
    body = f"Hi, the worflow {workflow_name} failed for the repo {repo_name}.please check the logs for more details.\nMore Details: \nRun_ID: {workflow_run_id}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

        print('Email send Successfully')
    except Exception as e:
        print(f'ERROR: {e}')

send_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))