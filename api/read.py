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
        organizations = []
        for i in user.get('idBoards'):
            boards.append(trello.boards.get(i))
            organizations.append(trello.boards.get(i).get('idOrganization'))
        return JsonResponse({'data': 'success', 'user': user, 'boards': boards, 'organizations': organizations})
    else:
        return JsonResponse({'data': 'Not Authenticated Yet'})

def get_user_organizations(request):
    account = Account.objects.get(user_id=request.user.id)
    if account.trello_token:
        trello = TrelloApi('8375d26f1323687c9c60a19ba6860aac')
        trello.set_token(account.trello_token)
        user = trello.members.get('me')
        organizations = []
        # import pdb; pdb.set_trace()
        for i in user.get('idOrganization'):
            organizations.append(trello.organizations.get(i))
        return JsonResponse({'data': 'success', 'user': user, 'organizations': organizations})
    else:
        return JsonResponse({'data': 'Not Authenticated Yet'})
