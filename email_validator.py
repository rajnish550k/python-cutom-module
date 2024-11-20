import re
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def validate_email(email):
    if re.match(EMAIL_REGEX, email):
        return True
    return False
import socket

def domain_exists(email):
    domain = email.split('@')[1]
    
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False
