from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Member
from django.core.exceptions import ValidationError

class MemberRegistrationForm(UserCreationForm):
    whatsapp_number = forms.CharField(
        max_length=20,
        required=True,
        help_text='Your WhatsApp number including country code (e.g., +27123456789)'
    )
    full_name = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(required=False)
    preferred_language = forms.ChoiceField(
        choices=Member.PreferredLanguage.choices,
        initial=Member.PreferredLanguage.ENGLISH
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'whatsapp_number', 'full_name', 'phone_number', 'email', 
                 'preferred_language', 'password1', 'password2']
    
    def clean_whatsapp_number(self):
        whatsapp_number = self.cleaned_data.get('whatsapp_number')
        if Member.objects.filter(whatsapp_number=whatsapp_number).exists():
            raise forms.ValidationError('This WhatsApp number is already registered.')
        return whatsapp_number

class UserProfileEditForm(forms.ModelForm):
    """Form for editing user profile information including username"""

    username = forms.CharField(
        max_length=150,
        required=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
    )
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Pre-populate form with existing data
            self.fields['username'].initial = self.instance.username
            self.fields['email'].initial = self.instance.email
            self.fields['first_name'].initial = self.instance.first_name
            self.fields['last_name'].initial = self.instance.last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Check if another user (not the current one) has this username
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise ValidationError('This username is already taken. Please choose a different one.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if another user (not the current one) has this email
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('This email address is already registered.')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            
            # Create member profile
            member = Member.objects.create(
                user=user,
                whatsapp_number=self.cleaned_data['whatsapp_number'],
                full_name=self.cleaned_data['full_name'],
                phone_number=self.cleaned_data.get('phone_number'),
                email=self.cleaned_data.get('email'),
                preferred_language=self.cleaned_data.get('preferred_language')
            )
        return user

class MemberProfileEditForm(forms.ModelForm):
    """Form for editing member profile information"""
    whatsapp_number = forms.CharField(
        max_length=20,
        required=True,
        help_text='Your WhatsApp number including country code (e.g., +27123456789)'
    )
    full_name = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(required=False)
    preferred_language = forms.ChoiceField(
        choices=Member.PreferredLanguage.choices,
        initial=Member.PreferredLanguage.ENGLISH
    )

    class Meta:
        model = Member
        fields = ['whatsapp_number', 'full_name', 'phone_number', 'email', 'preferred_language']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Pre-populate form with existing data
            self.fields['whatsapp_number'].initial = self.instance.whatsapp_number
            self.fields['full_name'].initial = self.instance.full_name
            self.fields['phone_number'].initial = self.instance.phone_number
            self.fields['email'].initial = self.instance.email
            self.fields['preferred_language'].initial = self.instance.preferred_language

    def clean_whatsapp_number(self):
        whatsapp_number = self.cleaned_data.get('whatsapp_number')
        # Check if another member (not the current one) has this whatsapp number
        if Member.objects.filter(whatsapp_number=whatsapp_number).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This WhatsApp number is already registered by another member.')
        return whatsapp_number