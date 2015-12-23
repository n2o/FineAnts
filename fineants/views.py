from django.shortcuts import render
from .models import Transaction


def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'fineants/list_transactions.html', {'transactions': transactions})