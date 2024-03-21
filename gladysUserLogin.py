"""
Student: Dang Le
Module: gladysUserLogin
Description: This module does …
"""
import re

def login():
    """
    document your function definition here. what does it do?
    """
    emailAddress = ""
    chkInput=True
    stregex = r'\b[A-Za-z0-9.]+@[A-Za-z0-9.-]+\.[A-Za-z][A-Za-z0-9]*\b'
    while chkInput:
        userName = input("Enter login username:")
        if(re.fullmatch(stregex, userName)):
            emailAddress = userName
            userPwd = input("Enter login password:")
            chkInput=False
        else:
            print("Invalid login username !!!") 

    return emailAddress
