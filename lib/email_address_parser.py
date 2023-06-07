import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_regex, self.email_string)
        return sorted(emails, key=lambda email: email.lower())
