from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django import forms


class EmailCheckForm123(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(EmailCheckForm123, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-email-form"
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.layout = Layout(
            Field("email", css_class="form-control"),
        )
