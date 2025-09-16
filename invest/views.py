from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def investments_main_view(request):
    """Main investments page"""
    context = {
        'user': request.user,
        'total_balance': 42580,
        'savings': 18400,
        'investments': 24180,
        'business_income': 12500,
        'current_date': timezone.now().strftime("%B %d, %Y"),
    }
    return render(request, 'invest/investments_main.html', context)

@login_required
def investment_projections_view(request):
    """Investment Projections view"""
    context = {
        'user': request.user,
        'investments': 24180,
    }
    return render(request, 'invest/investment_projections.html', context)
