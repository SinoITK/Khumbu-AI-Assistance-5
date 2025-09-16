from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def business_main_view(request):
    """Main business page"""
    return render(request, 'business/business_main.html')
