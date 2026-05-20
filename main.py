# Create an Email class with the following attributes:
# sender, receiver, subject, body, and has_been_read.
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True


class User:
    def __init__(self, name):
        self.name = name
        self.inbox = []

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)


class Inbox:
    def __init__(self):
        self.emails = []
