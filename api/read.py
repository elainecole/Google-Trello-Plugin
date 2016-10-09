from trello import TrelloApi
from api.models import Account
from django.http import JsonResponse

def get_user_boards(request):
    a = Account.objects.get(user_id=request.user.id)
    trello = TrelloApi('8375d26f1323687c9c60a19ba6860aac')
    trello.set_token(a.trello_token)
    # token_url = trello.get_token_url('Robin', expires='30days', write_access=True)
    # boards = trello.actions.get_board(trello)
    # response = trello.search.get(boards)
    # boards = trello.boards.get('y2OdMQl4')
    # cards = trello.cards()
    user = trello.members.get('me')
    boards = []
    for i in user.get('idBoards'):
        boards.append(trello.boards.get(i))
    return JsonResponse({'data': 'success', 'user': user, 'boards': boards})
