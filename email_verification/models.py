"""Module for creating models in application."""

from django.db import models

# Create your models here.


class Email(models.Model):
    """
    Model representing an email record.

    Attributes:
        email (CharField): The email address.
        score (IntegerField): The score associated with the email.
        status (CharField): The status of the email.
    """

    email = models.CharField(max_length=50)
    score = models.IntegerField()
    status = models.CharField(max_length=20)

    def __repr__(self):
        """
        Provide a string representation of the Email instance.

        Returns:
            str: A string representing the email address of the Email instance.
        """
        return self.email
