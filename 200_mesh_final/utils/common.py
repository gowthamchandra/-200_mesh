# -- coding: utf-8 --
"""
Declaring common functions
"""
import logging
import pytz
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.constants import IST_TIMEZONE
from utils.settings import SENDER_ID, SENDER_PASSWORD, SMTP_SERVER, SMTP_PORT,PRED_MAIL_RECIPIENTS,PRED_MAIL_SUBJECT,PRED_CC_RECIPIENTS,PRED_ERROR_SUBJECT,ERR_MAIL_RECIPIENTS

# configuring logger



def get_current_datetime():
    """
    Returns the current local datetime.
    :return: current localtime objectDB_HOST
    """
    return datetime.now(pytz.timezone(IST_TIMEZONE))


# def sendmail(emaillist,cc content, subject):
#     """
#     Sends Email to the given recipients with the given content
#     :param emaillist: email recipients
#     :param content: email content
#     :param subject: email subject
#     :return:
#     """
#     for email in emaillist:
# #         LOG.info("Sending email for: %s", email)
#         # Initialising Config
#         smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#         smtpserver.starttls()
#         smtpserver.login(SENDER_ID, SENDER_PASSWORD)
#         msg = MIMEMultipart()
#         msg['From'] = SENDER_ID
#         msg['To'] = email
#         msg['Cc']=Cc
#         msg['Subject'] = subject
#         msg.attach(MIMEText(content, _subtype='html'))
#         smtpserver.sendmail(SENDER_ID, email, msg.as_string())
#         smtpserver.close()
# #     LOG.info("Emails Sent!")

def sendmail(emaillist, cc_list, content, subject):
    """
    Sends Email to the given recipients with the given content
    :param emaillist: email recipients
    :param cc_list: CC email recipients
    :param content: email content
    :param subject: email subject
    :return:
    """
    # Initializing Config
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.starttls()
    smtpserver.login(SENDER_ID, SENDER_PASSWORD)
    msg = MIMEMultipart()
    msg['From'] = SENDER_ID
    msg['To'] = ",".join(emaillist)
    msg['Cc'] = ",".join(cc_list)
    msg['Subject'] = subject
    msg.attach(MIMEText(content, _subtype='html'))

    # Send a single email to all recipients and CCs
    smtpserver.sendmail(SENDER_ID, emaillist + cc_list, msg.as_string())
    smtpserver.close()

# def sendmail(emaillist, cc_list, content, subject):
#     """
#     Sends Email to the given recipients with the given content
#     :param emaillist: email recipients
#     :param cc_list: CC email recipients
#     :param content: email content
#     :param subject: email subject
#     :return:
#     """
#     for email in emaillist:
#         # LOG.info("Sending email for: %s", email)
#         # Initializing Config
#         smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#         smtpserver.starttls()
#         smtpserver.login(SENDER_ID, SENDER_PASSWORD)
#         msg = MIMEMultipart()
#         msg['From'] = SENDER_ID
#         msg['To'] = email
#         msg['Cc'] = ",".join(cc_list)
#         msg['Subject'] = subject
#         msg.attach(MIMEText(content, _subtype='html'))

#         # Include both main recipients and CC recipients in the sendmail call
#         smtpserver.sendmail(SENDER_ID, [email] + cc_list, msg.as_string())
#         smtpserver.close()
        
        
def mail_precip_preds(tomorrow, predict_shift, ped):
    # ... [previous parts of the function]

    # Email Content
    content = "<html><body>"
    content += "<h2>Predictive Alert: PSD Forecast in Alumina Precipitation</h2>"
    content += "<p>Dear Plant Operations Team,</p>"
    content += "<p>This email provides the forecasted PSD values for the alumina precipitation process:</p>"
    content += "<ul>"
    content += "<li>Forecast Date: <strong>{}</strong></li>".format(tomorrow)
    content += "<li>Shift: <strong>{}</strong></li>".format(predict_shift)


    content += "<li>Predicted PSD Value: <strong>{}</strong></li>".format(ped)

    content += "</ul>"
#     content += "<p>Please note: This is a part of ongoing plant trials and predictive modelling efforts. Do not act on these predictions without further analysis and consultation.</p>"
    content += "<p>Please note: Please consider this as part of validating the model.</p>"
    
    content += "<p>This is an automated email. For queries or clarifications, please contact: <a href='mailto:ashok.gudipadu-v@adityabirla.com'>ashok.gudipadu-v@adityabirla.com</a></p>"
    content += "<p>Thank you,<br>GDNA Team</p>"
    content += "</body></html>"
    
    mail_recipients = PRED_MAIL_RECIPIENTS.split(",")
    CC_recipients = PRED_CC_RECIPIENTS.split(",")

    sendmail(mail_recipients,CC_recipients,content, PRED_MAIL_SUBJECT)
    
def mail_exception(exception):
    try:
        # Prepare the email content
        content = "<html><body>"
        content += "<h2>Alert: Exception in Main Function</h2>"
        content += "<p>Dear Team,</p>"
        content += "<p>An exception occurred in the main function:</p>"
        content += f"<p><strong>Exception Details:</strong> {str(exception)}</p>"
        content += "<p>Thank you,<br>Your Team</p>"
        content += "</body></html>"

        subject = "Belagavi_Precipitation || Exception Alert in Predictive model"
        mail_recipients = ERR_MAIL_RECIPIENTS.split(",")
        CC_recipients = PRED_CC_RECIPIENTS.split(",")
        # Send the email
        sendmail(mail_recipients,CC_recipients, content, subject)

    except Exception as e:
        raise Exception(f"Error occurred in mail_exception: {e}")


