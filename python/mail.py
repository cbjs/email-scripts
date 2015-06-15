#!/usr/bin/python
#coding:utf-8
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.Utils import formatdate
from email import encoders
import mimetypes
import os
from smtplib import SMTP

class Email(object):
    """Email Class"""
    def __init__(self, smtp = 'localhost', username = '', password = ''):
        self.smtp = smtp
        self.username = username
        self.password = password

    def send(self, 
             sender,                    # from email address
             receiptors,                # email target address list
             cc = [],                   # cc target address list
             bcc = [],                  # bcc target address list
             subject = 'no subject',    # email subject
             content = '',              # email content, encoding must be utf8
             content_subtype = 'plain', # content type [plain, html]
             embed_images = [], 		# embeded images [{id:'image-id', path:'/p/to/i.png'}, ..]
             attachment = []):          # attachment file list
        """ Send mail function"""
        # process mail message meta
        message = MIMEMultipart()
        message['From'] = sender
        if isinstance(receiptors, list):
            message['To'] = ', '.join(receiptors)
        else:
            message['To'] = receiptors
            receiptors = [receiptors]
        if isinstance(cc, list):
            message['CC'] = ', '.join(cc)
            receiptors.extend(cc)
        else:
            message['CC'] = cc
            receiptors.append(cc)
        if isinstance(bcc, list):
            message['BCC'] = ', '.join(bcc)
            receiptors.extend(bcc)
        else:
            message['BCC'] = bcc
            receiptors.append(bcc)
        message['Subject'] = subject
        message['Date'] = formatdate(localtime=True)
        if content:
            message.attach(MIMEText(content.encode('utf-8'), content_subtype, 'utf-8')) 
        for embed_image in embed_images: 
            with file(embed_image['path'], 'rb') as image_file: 
                mime_image = MIMEImage(image_file.read()) 
                mime_image.add_header('Content-ID', embed_image['id']) 
                message.attach(mime_image)

        # process attachment
        if attachment:
            if not isinstance(attachment, list):
                attachment = [attachment]
            for attach_filename in attachment:
                if not os.path.isfile(attach_filename):
                    continue
                ftype, encoding = mimetypes.guess_type(attach_filename)
                if ftype is None or encoding is not None:
                    ftype = "application/octet-stream"
                main_type, sub_type = ftype.split('/', 1)
                with file(attach_filename, 'rb') as attach_file:
                    if main_type == 'text':
                        attachment_message = MIMEText(attach_file.read())
                    elif main_type == 'image':
                        attachment_message = MIMEImage(attach_file.read())
                    elif main_type == 'audio':
                        attachment_message = MIMEAudio(attach_file.read())
                    else:
                        attachment_message = MIMEBase(main_type, sub_type)
                        attachment_message.set_payload(attach_file.read())
                        encoders.encode_base64(attachment_message)
                    attachment_message.add_header('Content-Disposition',
                                                  'attachment',
                                                  filename=os.path.basename(attach_filename))
                    message.attach(attachment_message)
        # send mail
        mail_server = SMTP(self.smtp)
        if self.username:
            mail_server.login(self.username, self.password)
        mail_server.sendmail(sender, receiptors, message.as_string())
        mail_server.quit()
