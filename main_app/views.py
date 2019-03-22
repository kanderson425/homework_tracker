from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from main_app.forms import FeedbackForm
import uuid
import boto3
from main_app.models import Assignment, Objective, Photo



def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class assignmentCreate(LoginRequiredMixin, CreateView):
    model = Assignment
    fields = ['name', 'github_url', 'status', 'description', 'objectives']
    success_url = '/assignments/'   
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 

class assignmentUpdate(LoginRequiredMixin,UpdateView):
    model = Assignment
    fields = ['name', 'github_url', 'status', 'description', 'objectives']

class assignmentDelete(LoginRequiredMixin,DeleteView):
    model = Assignment
    success_url = '/assignments/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def assignments_index(request):
    assignments = Assignment.objects.filter(user=request.user)
    return render(request, 'assignments/index.html', { 'assignments': assignments })

@login_required
def assignments_detail(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    objectives_assignment_doesnt_have = Objective.objects.exclude(id__in = assignment.objectives.all().values_list('id'))
    feedback_form = FeedbackForm()
    return render(request, 'assignments/detail.html', { 
        'assignment': assignment, 
        'feeedback_form': feedback_form,
        'objectives': objectives_assignment_doesnt_have
    })

@login_required
def add_feedback(request, assignment_id):
    print('hello')
    form = FeedbackForm(request.POST)
    if form.is_valid():
        new_feedback = form.save(commit=False)
        new_feedback.assignment_id = assignment_id
        new_feedback.save()
    else:
        msg = 'Errors: %s' % form.errors.as_text()
        print(msg)  
    return redirect('detail', assignment_id=assignment_id)

@login_required
def add_photo(request, assignment_id):
	# photo-file was the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object
            photo = Photo(url=url, assignment_id=assignment_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', assignment_id=assignment_id)

class objectiveList(LoginRequiredMixin, ListView):
    model = Objective

class objectiveDetail(LoginRequiredMixin, DetailView):
    model = Objective

class objectiveCreate(LoginRequiredMixin, CreateView):
    model = Objective
    fields = '__all__'

class objectiveUpdate(LoginRequiredMixin, UpdateView):
    model = Objective 
    fields = '__all__'

class objectiveDelete(LoginRequiredMixin, DeleteView):
    model = Objective 
    success_url = '/objectives/'

@login_required
def assoc_objective(request, assignment_id, objective_id):
    Assignment.objects.get(id=assignment_id).objectives.add(objective_id)
    return redirect('detail', assignment_id=assignment_id)

@login_required
def unassoc_objective(request, assignment_id, objective_id):
    Assignment.objects.get(id=assignment_id).objectives.remove(objective_id)
    return redirect('detail', assignment_id=assignment_id)


