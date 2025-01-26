from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Generate and send verification PIN
            profile = Profile.objects.get(user=user)
            profile.generate_verification_pin()
            send_mail(
                'Your Verification PIN',
                f'Your verification PIN is: {profile.verification_pin}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            return redirect('verify_email')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def verify_email(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
        try:
            profile = Profile.objects.get(verification_pin=pin)
            profile.is_verified = True
            profile.verification_pin = None  # Clear the PIN after use
            profile.save()
            return redirect('login')
        except Profile.DoesNotExist:
            return render(request, 'verify_email.html', {'error': 'Invalid PIN'})
    return render(request, 'verify_email.html')




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.profile.is_verified:  # Ensure the user is verified
                    login(request, user)
                    return redirect('dashboard')  # Redirect to the dashboard or home page
                else:
                    return render(request, 'login.html', {
                        'form': form,
                        'error': 'Your account is not verified. Please check your email.',
                    })
            else:
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'Invalid username or password.',
                })
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
