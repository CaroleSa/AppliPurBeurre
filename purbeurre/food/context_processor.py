from django.conf import settings

def menu(request):
    if request.user.is_authenticated:
        return {'authenticated': 'True'}
    else:
        return {'authenticated': 'False'}