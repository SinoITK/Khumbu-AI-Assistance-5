from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def travel_main_view(request):
    """Main travel page"""
    return render(request, 'travel/travel_main.html')
