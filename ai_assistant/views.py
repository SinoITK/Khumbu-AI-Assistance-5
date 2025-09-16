from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def ai_assistant_view(request):
    """AI Assistant view"""
    return render(request, 'ai_assistant/ai_assistant.html')
