"""Module for creating forms."""

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django import forms


class EmailCheckForm(forms.Form):
    """
    A Django form for checking an email address.

    This form provides a field to input an email address that will be checked
    for certain criteria or validity. It is styled and configured using crispy forms.

    Attributes:
        email (EmailField): A field to input the email address to be checked.
    """

    email = forms.EmailField(label="Email to check")

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with custom settings.

        Sets up the form helper and layout for crispy forms rendering.

        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-email-form"
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.layout = Layout(
            Field("email", css_class="form-control"),
        )


class EmailDeleteForm(forms.Form):
    """
    A Django form for deleting an email address.

     This form provides a field to input an email address that will be deleted
     from a system or database. It uses crispy forms for improved layout and styling.

     Attributes:
         email (EmailField): A field to input the email address to be deleted.
    """

    email = forms.EmailField(label="Email to delete")

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with custom settings.

        Configures the form helper and layout specifically for the delete operation,
        including a 'Delete' button styled with a 'btn-danger' class.

        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-email-form"
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Delete", css_class="btn-danger"))
        self.helper.layout = Layout(
            Field("email", css_class="form-control"),
        )
