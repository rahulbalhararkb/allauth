from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import SignUpForm

# Create your views here.
User = get_user_model()

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup_form.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

@login_required
def home(request):
	return render(request, 'myapp/home.html')