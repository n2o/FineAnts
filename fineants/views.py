from django.shortcuts import render, get_list_or_404
from .models import Transaction


def list_transactions(request):
    transactions = get_list_or_404(Transaction.objects.order_by('created'))
    return render(request, 'fineants/list_transactions.html', {'transactions': transactions})