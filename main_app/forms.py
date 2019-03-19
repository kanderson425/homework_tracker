from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .choices import USERTYPE_CHOICES, LOCATION_CHOICES, CLASSTYPE_CHOICES, DATE_CHOICES
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='', help_text='', widget=forms.TextInput(attrs={"placeholder": "Input your first name"}))
    last_name = forms.CharField(max_length=30, label='', help_text='', widget=forms.TextInput(attrs={"placeholder": "Input your last name"}))
    # username = forms.CharField(max_length=30, label='', help_text='', widget=forms.TextInput(attrs={"placeholder": "Input username"}))
    email = forms.EmailField(max_length=250, label='', help_text='', widget=forms.TextInput(attrs={"placeholder": "Input your email"}))

    usertype = forms.CharField(
        label= "Student or Instructor",
        initial = '',
        widget=forms.Select(choices=USERTYPE_CHOICES)
    )

    location = forms.CharField(
        label="What City is your cohort in?",
        widget=forms.Select(choices=LOCATION_CHOICES)
    )

    class_start_date = forms.DateField(
        widget = forms.Select(choices=DATE_CHOICES),
    )

    class_type = forms.CharField(
        label = "Class Type",
        initial= '',
        widget = forms.Select(choices=CLASSTYPE_CHOICES)
    )

    # password1 = forms.CharField(max_length=30, label='', help_text='', widget=forms.PasswordInput(attrs={"placeholder": "Input your password"}))
    # password2 = forms.CharField(max_length=30, label='', help_text='', widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password"}))

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            # 'username',
            'email',
            'usertype',
            'location',
            'class_start_date',
            'class_type',
            # 'password1',
            # 'password2'
        ]

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    FormActions(
        Submit('save_changes', 'Save changes', css_class="btn-primary"),
        Submit('cancel', 'Cancel'),
    )
    # )

# class MessageForm(forms.Form):
#     text_input = forms.CharField()

#     textarea = forms.CharField(
#         widget = forms.Textarea(),
#     )

#     radio_buttons = forms.ChoiceField(
#         choices = (
#             ('option_one', "Option one is this and that be sure to include why it's great"),
#             ('option_two', "Option two can is something else and selecting it will deselect option one")
#         ),
#         widget = forms.RadioSelect,
#         initial = 'option_two',
#     )

#     checkboxes = forms.MultipleChoiceField(
#         choices = (
#             ('option_one', "Option one is this and that be sure to include why it's great"),
#             ('option_two', 'Option two can also be checked and included in form results'),
#             ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
#         ),
#         initial = 'option_one',
#         widget = forms.CheckboxSelectMultiple,
#         help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
#     )

#     appended_text = forms.CharField(
#         help_text = "Here's more help text"
#     )

#     prepended_text = forms.CharField()

#     prepended_text_two = forms.CharField()

#     multicolon_select = forms.MultipleChoiceField(
#         choices = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
#     )

#     # Uni-form
#     helper = FormHelper()
#     helper.form_class = 'form-horizontal'
#     helper.layout = Layout(
#         Field('text_input', css_class='input-xlarge'),
#         Field('textarea', rows="3", css_class='input-xlarge'),
#         'radio_buttons',
#         Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
#         AppendedText('appended_text', '.00'),
#         PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
#         PrependedText('prepended_text_two', '@'),
#         'multicolon_select',
#         FormActions(
#             Submit('save_changes', 'Save changes', css_class="btn-primary"),
#             Submit('cancel', 'Cancel'),
#         )
#     )
