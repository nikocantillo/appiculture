"""Users views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import login, authenticate, logout #add this
# Models
from django.contrib.auth.models import User
from courses.models import Course
from .models import User as Profile

# Forms
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm #add this
from django.shortcuts import  render, redirect
from django.contrib import messages


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'courses/pages/course/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's Courses to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['Courses'] = Course.objects.filter(user=user).order_by('-created')
        return context


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'authentication/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


# class UpdateProfileView(LoginRequiredMixin, UpdateView):
#     """Update profile view."""

#     template_name = 'users/update_profile.html'
#     model = Profile
#     fields = ['website', 'biography', 'phone_number', 'picture']

#     def get_object(self):
#         """Return user's profile."""
#         return self.request.user.profile

#     def get_success_url(self):
#         """Return to user's profile."""
#         username = self.object.user.username
#         return reverse('users:detail', kwargs={'username': username})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="authentication/signin.html", context={"login_form":form})