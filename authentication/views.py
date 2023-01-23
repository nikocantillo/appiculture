"""Users views."""

# Django
import uuid
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
# hola este es un comentariio
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.views.generic.base import TemplateView
from authentication.utils.send_mail import create_mail
from django.shortcuts import resolve_url
from django.conf import settings
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import FormView



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
			user = authenticate(
                username=username, 
                password=password
            )
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(
        request=request, 
        template_name="authentication/signin.html", 
        context={"form":form}
    )


def password_reset_request(request):

	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))

			token = str(uuid.uuid4())
			if associated_users.exists():
				for user in associated_users:
					token_user = Profile.objects.get(user=user.pk)
					token_user.forget_password_token = token
					token_user.save()
					subject = "Password Reset Requested"
					# email_template_name = "authentication/password_reset.txt"
					c = {
					# "email":user.email,
					'domain':'127.0.0.1:8000',
					# 'site_name': 'Website',
					# "user": user,
					'token': token,
					'protocol': 'http',
					}
					try:
						mail = create_mail(user.email, subject, 'authentication/mail/mail.html' , c)
						mail.send(fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect('users:password_reset_done')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="authentication/password_reset.html", context={"password_reset_form":password_reset_form})

def change_password(request, token):
	context = {}

	try:
		profile = Profile.objects.filter(forget_password_token = token).first()
		if request.method == 'POST':
			new_password = request.POST.get('new_password')
			confirm_password = request.POST.get('confirm_password')
			user_id = request.POST.get('user_id')

			if user_id is None:
				messages.success(request, 'EL id del Usuario no fue encontrado')
				return redirect(f'/password_reset_confirm/{token}/')
			
			if new_password != confirm_password:
				messages.success(request, 'Las Contraseñas deben ser iguales')
				return redirect(f'/password_reset_confirm/{token}/')

			user_id = User.objects.get(id = user_id)
			user_id.set_password(new_password)
			user_id.save()

			return redirect('users:login')


		context = {'user_id': profile.user.id}

	except Exception as e:
		print(e)
	
	return render(request, "authentication/password_reset_confirm.html", context)

class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {"user_id": self.user.id, "subtitle": None, **(self.extra_context or {})}
        )
        return context

class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = "authentication/password_reset_complete.html"
    title = _("Password reset complete")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_url"] = resolve_url(settings.LOGIN_URL)
        return context