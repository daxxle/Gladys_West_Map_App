
import re
from getpass import getpass

"""
Student: Dang Le
Module: gladysUserLogin
Description: This module does check user/password login valid/invalid
Valid login user should be an email address
"""

def login():
    """
    document your function definition here. what does it do?
    """
    emailAddress = ""
    userPwd=""
    chkInput=True
    stregex = r'\b[A-Za-z0-9.]+@[A-Za-z0-9.-]+\.[A-Za-z][A-Za-z0-9]*\b'
    while chkInput:
        userName = input("Enter login username:")
        if(re.fullmatch(stregex, userName)):
            emailAddress = userName
            userPwd = getpass("Enter login password:")
            chkInput=False
        else:
            print("ERROR: User login is not an email address !!!") 

    return emailAddress
