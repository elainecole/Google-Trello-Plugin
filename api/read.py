from trello import TrelloApi
from api.models import Account
from django.http import JsonResponse

def get_user_boards(request):
    a = Account.objects.get(user_id=request.user.id)
    trello = TrelloApi('8375d26f1323687c9c60a19ba6860aac')
    trello.set_token(a.trello_token)
    boards = trello.boards.get('y2OdMQl4')
    import pdb; pdb.set_trace()
    return JsonResponse({'data': 'success'})
