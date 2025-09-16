from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def savings_dashboard_view(request):
    """Integrated Savings Overview view"""
    context = {
        'user': request.user,
    }
    return render(request, 'savings/savings_dashboard.html', context)

@login_required
def stokvel_transactions_view(request):
    """Day-to-day stokvel transactions view"""
    context = {
        'user': request.user,
    }
    return render(request, 'savings/stokvel_transactions.html', context)
