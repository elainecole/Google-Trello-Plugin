from trello import TrelloApi
from api.models import Account
from django.http import JsonResponse

def get_user_boards(request):
    account = Account.objects.get(user_id=request.user.id)
    if account.trello_token:
        trello = TrelloApi('8375d26f1323687c9c60a19ba6860aac')
        trello.set_token(account.trello_token)
        user = trello.members.get('me')
        boards = []
        for i in user.get('idBoards'):
            boards.append(trello.boards.get(i))
        return JsonResponse({'data': 'success', 'user': user, 'boards': boards})
    else:
        return JsonResponse({'data': 'Not Authenticated Yet'})
