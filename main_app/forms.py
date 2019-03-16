from django.forms import ModelForm
from .models import User, Location
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = models.EmailField(required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'location', 'class_start_date', 'class_type', 'password1', 'password2')
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = cleaned_data('first_name')
        user.last_name = cleaned_data('last_name')
        user.email = cleaned_data('email')
        if commit:
            user.save()
