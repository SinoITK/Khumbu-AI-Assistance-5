from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import MemberRegistrationForm, MemberProfileEditForm, UserProfileEditForm
from .models import Member, UserPreferences, LoginHistory
import json

def landing_page(request):
    """Landing page view for non-authenticated users"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'dashboard/landing.html')

@login_required
def dashboard_view(request):
    # Sample data for the dashboard
    context = {
        'user': request.user,
        'total_balance': 42580,
        'savings': 18400,
        'investments': 24180,
        'business_income': 12500,
        'current_date': timezone.now().strftime("%B %d, %Y"),
        'expense_coverage': 75,  # Percentage of travel expenses covered
    }
    return render(request, 'dashboard/index.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def register_view(request):
    """User registration view"""
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Khumbulekhaya.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MemberRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    """User profile view"""
    preferences, created = UserPreferences.objects.get_or_create(user=request.user)

    context = {
        'user': request.user,
        'member_since': request.user.date_joined.strftime("%B %Y"),
        'last_login': request.user.last_login.strftime("%B %d, %Y at %I:%M %p") if request.user.last_login else "Never",
        'preferences': preferences,
    }
    return render(request, 'dashboard/profile.html', context)

@login_required
def profile_edit_view(request):
    """User profile edit view"""
    try:
        member = request.user.member_profile
    except Member.DoesNotExist:
        messages.error(request, 'Profile not found. Please contact support.')
        return redirect('profile')

    if request.method == 'POST':
        form = MemberProfileEditForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MemberProfileEditForm(instance=member)

    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'dashboard/profile_edit.html', context)

@login_required
def user_profile_edit_view(request):
    """User profile edit view for username and basic user fields"""
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileEditForm(instance=request.user)

    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'dashboard/user_profile_edit.html', context)

@login_required
def change_password_view(request):
    """Change user password view"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'dashboard/change_password.html', context)

@login_required
def login_history_view(request):
    """View user login history"""
    login_history = LoginHistory.objects.filter(user=request.user)[:20]  # Last 20 logins

    context = {
        'login_history': login_history,
        'user': request.user,
    }
    return render(request, 'dashboard/login_history.html', context)

@login_required
def two_factor_setup_view(request):
    """Two-factor authentication setup view"""
    preferences, created = UserPreferences.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'enable':
            # In a real implementation, you'd generate a TOTP secret here
            # For now, we'll just toggle the setting
            preferences.two_factor_enabled = True
            preferences.save()
            messages.success(request, 'Two-factor authentication has been enabled!')
        elif action == 'disable':
            preferences.two_factor_enabled = False
            preferences.two_factor_secret = None
            preferences.save()
            messages.success(request, 'Two-factor authentication has been disabled!')

        return redirect('profile')

    context = {
        'preferences': preferences,
        'user': request.user,
    }
    return render(request, 'dashboard/two_factor_setup.html', context)

@login_required
@require_POST
def update_preferences_view(request):
    """AJAX view to update user preferences"""
    try:
        data = json.loads(request.body)
        preferences, created = UserPreferences.objects.get_or_create(user=request.user)

        if 'dark_mode' in data:
            preferences.dark_mode = data['dark_mode']
        if 'email_notifications' in data:
            preferences.email_notifications = data['email_notifications']

        preferences.save()

        return JsonResponse({'success': True, 'message': 'Preferences updated successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)


