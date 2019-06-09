# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:38:29 2019

@author: gvandeyk
"""

# Import the email modules we'll need
from email.parser import BytesParser, Parser
from email.policy import default


def readEmailFile(Emailfile):
    # e-mail is in a file
    with open(Emailfile, 'rb') as fp:
        msg = BytesParser(policy=default).parse(fp)
    return msg  # returns an object of type email.message.EmailMessage


def storeEmailHeaderInfo(TheEmailMessage):
    emailHeaderInfo = {'Sender': TheEmailMessage['to'],
                       'Receiver': TheEmailMessage['from'],
                       'CC_Receiver': TheEmailMessage['cc'],
                       'BCC_Receiver': TheEmailMessage['bcc'],
                       'Subject': TheEmailMessage['subject']
                       }
    return emailHeaderInfo  # Type dictionary


def getEmailBody(TheEmailMessage):
    return TheEmailMessage.get_body()


if __name__ == '__main__':
    # This is for testing purposes :
    messagepath = 'C:/Users/gvandeyk/OneDrive - DXC Production/Downloads/'
    messagefile = messagepath + 'SomeEmail.txt'
    MyEmail = readEmailFile(messagefile)
    print(storeEmailHeaderInfo(MyEmail))
    print("----------------------------")
    print(getEmailBody(MyEmail))
