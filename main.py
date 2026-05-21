import datetime


class Email:
    """Represents a single email message with sender, receiver, and content."""

    def __init__(self, sender, receiver, subject, body):
        """Initialize a new email.

        Args:
            sender (User): The user sending the email.
            receiver (User): The user receiving the email.
            subject (str): Email subject line.
            body (str): Email body content.
        """
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self):
        """Mark the email as read."""
        self.read = True

    def display_full_email(self):
        """Display the full email content and mark it as read."""
        self.mark_as_read()

        print("\n--- Email ---")
        print(f"From: {self.sender.name}")
        print(f"To: {self.receiver.name}")
        print(f"Subject: {self.subject}")
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f"Body: {self.body}")
        print("------------\n")

    def __str__(self):
        """Return a concise string representation for inbox listings."""
        status = "Read" if self.read else "Unread"
        return (
            f"[{status}] From: {self.sender.name} | "
            f"Subject: {self.subject} | "
            f"Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
        )


class Inbox:
    """Manages a collection of emails for a user."""

    def __init__(self):
        """Initialize an empty inbox."""
        self.emails = []

    def receive_email(self, email):
        """Add a new email to the inbox.

        Args:
            email (Email): The email object to store.
        """
        self.emails.append(email)

    def list_emails(self):
        """Display all emails in the inbox with numbering."""
        if not self.emails:
            print("Your inbox is empty.\n")
            return

        print("\nYour Emails:")
        for i, email in enumerate(self.emails, start=1):
            print(f"{i}. {email}")

    def read_email(self, index):
        """Display the full content of an email by its list index.

        Args:
            index (int): 1-based index of the email to read.
        """
        if not self.emails:
            print("Inbox is empty.\n")
            return

        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")
            return

        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        """Delete an email from the inbox by its list index.

        Args:
            index (int): 1-based index of the email to delete.
        """
        if not self.emails:
            print("Inbox is empty.\n")
            return

        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")
            return

        del self.emails[actual_index]
        print("Email deleted.\n")


class User:
    """Represents a user with an email inbox and sending capabilities."""

    def __init__(self, name):
        """Initialize a new user.

        Args:
            name (str): The user's display name.
        """
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        """Send an email to another user.

        Args:
            receiver (User): The recipient user.
            subject (str): Subject of the email.
            body (str): Body content of the email.
        """
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f"Email sent from {self.name} to {receiver.name}!\n")

    def check_inbox(self):
        """Display the user's inbox contents."""
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        """Read a specific email from the user's inbox.

        Args:
            index (int): 1-based index of the email to read.
        """
        self.inbox.read_email(index)

    def delete_email(self, index):
        """Delete a specific email from the user's inbox.

        Args:
            index (int): 1-based index of the email to delete.
        """
        self.inbox.delete_email(index)


def main():
    """Demonstrate the email system with sample users and interactions."""
    tory = User("Tory")
    ramy = User("Ramy")

    # Sample email exchange
    tory.send_email(ramy, "Hello", "Hi Ramy, just saying hello!")
    ramy.send_email(tory, "Re: Hello", "Hi Tory, hope you are fine.")

    # Demo inbox operations
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()


if __name__ == "__main__":
    main()
