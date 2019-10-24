from django.shortcuts import render


def create_account(request):

    return render(request, 'account/create_account.html')