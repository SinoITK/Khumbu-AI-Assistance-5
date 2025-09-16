import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.conf import settings

class Member(models.Model):
    
    class StokvelTier(models.TextChoices):
        SAVINGS = 'Savings', 'Savings'
        INVESTMENT = 'Investment', 'Investment'
        WEALTH = 'Wealth', 'Wealth'
    
    class StokvelStatus(models.TextChoices):
        ACTIVE = 'Active', 'Active'
        SUSPENDED = 'Suspended', 'Suspended'
        EXITED = 'Exited', 'Exited'
    
    class KYCStatus(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        VERIFIED = 'Verified', 'Verified'
        REJECTED = 'Rejected', 'Rejected'
    
    class PreferredLanguage(models.TextChoices):
        ENGLISH = 'en', 'English'
        ZULU = 'zu', 'Zulu'
        XHOSA = 'xh', 'Xhosa'
        AFRIKAANS = 'af', 'Afrikaans'
    
    member_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member_profile')
    whatsapp_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    stokvel_tier = models.CharField(max_length=20, choices=StokvelTier.choices, default=StokvelTier.SAVINGS)
    stokvel_status = models.CharField(max_length=20, choices=StokvelStatus.choices, default=StokvelStatus.ACTIVE)
    kyc_status = models.CharField(max_length=20, choices=KYCStatus.choices, default=KYCStatus.PENDING)
    id_image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_auth_at = models.DateTimeField(auto_now=True)
    preferred_language = models.CharField(max_length=2, choices=PreferredLanguage.choices, default=PreferredLanguage.ENGLISH)
    biometric_id = models.CharField(max_length=255, blank=True, null=True)
    join_date = models.DateField(default=timezone.now)
    total_savings = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    total_investment = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    stokfella_reference_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.full_name} ({self.whatsapp_number})"
    
    def save(self, *args, **kwargs):
        if not self.stokfella_reference_number:
            self.stokfella_reference_number = f"STKF{str(self.member_id)[:8].upper().replace('-', '')}"
        super().save(*args, **kwargs)


class UserPreferences(models.Model):
    """User preferences for notifications, theme, and other settings"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='preferences')
    email_notifications = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    two_factor_enabled = models.BooleanField(default=False)
    two_factor_secret = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Preferences for {self.user.username}"


class LoginHistory(models.Model):
    """Track user login history for security"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_history')
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    device_type = models.CharField(max_length=50, blank=True)
    login_time = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=True)

    class Meta:
        ordering = ['-login_time']

    def __str__(self):
        return f"{self.user.username} - {self.login_time}"
