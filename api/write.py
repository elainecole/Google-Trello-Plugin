from api.models import Account
from django.http import JsonResponse

def store_trello_token(request):
    token = request.POST['token']

    a = Account.objects.get(user_id=request.user.id)
    a.trello_token = token
    a.save()

    return JsonResponse({'token': token})
