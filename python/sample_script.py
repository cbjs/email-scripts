#!/usr/bin/python
#coding:utf-8
import os
import sys
from datetime import *
from urlparse import urlparse
from jinja2 import Environment, FileSystemLoader
from mail import Email

if __name__ == "__main__":
    # get data
    log_result = 

    # generate using jinja2 template
    env = Environment(loader = FileSystemLoader('%s/templates' % os.path.dirname(os.path.abspath(__file__))))
    template = env.get_template('html.email.tpl')
    html_content = template.render(result = log_result)

    # mail 
    email = Email(smtp = 'smtp.company.com') 
    email.send(sender = 'sender@company.com',
              receiptors = ["r1@company.com", "r2@company.com", "r3@company.com"],
              cc = 'c1@company.com',
              subject = 'email subject',
              content = html_content,
              content_subtype = 'html',
              attachment = ['/file/path/to/attachment'])
