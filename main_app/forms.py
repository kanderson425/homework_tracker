from django.forms import ModelForm
from main_app.models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['date', 'comment']

