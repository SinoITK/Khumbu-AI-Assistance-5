from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'whatsapp_number', 'stokvel_tier', 'stokvel_status', 'kyc_status', 'join_date']
    list_filter = ['stokvel_tier', 'stokvel_status', 'kyc_status', 'preferred_language']
    search_fields = ['full_name', 'whatsapp_number', 'email', 'phone_number']
    readonly_fields = ['member_id', 'created_at', 'last_auth_at', 'stokfella_reference_number']
    fieldsets = [
        ('Personal Information', {
            'fields': ['user', 'whatsapp_number', 'full_name', 'phone_number', 'email', 'preferred_language']
        }),
        ('Stokvel Information', {
            'fields': ['stokvel_tier', 'stokvel_status', 'kyc_status', 'join_date']
        }),
        ('Financial Information', {
            'fields': ['total_savings', 'total_investment']
        }),
        ('System Information', {
            'fields': ['member_id', 'stokfella_reference_number', 'created_at', 'last_auth_at'],
            'classes': ['collapse']
        }),
        ('Additional Information', {
            'fields': ['id_image_url', 'biometric_id'],
            'classes': ['collapse']
        })
    ]
