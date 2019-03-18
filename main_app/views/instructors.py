from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from forms import InstructorSignUpForm


class InstructorSignUpView(CreateView):
    model = User
    form_class = InstructorSignUpForm
    template_name = 'registration/instructor-signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'instructor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('instructors:cohort_select')