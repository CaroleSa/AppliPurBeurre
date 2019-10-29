from django.shortcuts import render
from account.forms import Account
from account.models import User
import hashlib




def account(request):
    form = Account()
    context = {'form': form}

    return render(request, 'account/account.html', context)




def create_account(request):
    form = Account()
    context = {'form': form}

    if request.method == 'POST':
        form = Account(request.POST)

        if form.is_valid():
            # get user's e-mail
            email = form.cleaned_data['e_mail']

            # get and encrypted user's password
            password = form.cleaned_data['password'].encode()
            encrypted_password = hashlib.sha1(password).hexdigest()

            # insert user's data in the database
            User.objects.create(e_mail=email, password=encrypted_password)

        else:
            # Form data doesn't match the expected format.
            # Add errors to the template.
            context["error"] = "Message d'erreur"

    return render(request, 'account/create_account.html', context)