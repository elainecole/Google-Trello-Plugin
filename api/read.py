from trello import TrelloApi
from api.models import Account
from django.http import JsonResponse
from apiclient.discovery import build
import httplib2
from oauth2client import client


def get_user_boards(request):
    account = Account.objects.get(user_id=request.user.id)
    if account.trello_token:
        trello = TrelloApi('1c4e6885b9d06b44eff07db8fb63b45f')
        trello.set_token(account.trello_token)
        user = trello.members.get('me')
        boards = []
        organizations = []
        lists = []
        cards = []
        for j in user.get('idOrganizations'):
            organizations.append(trello.organizations.get(j))
        for i in user.get('idBoards'):
            boards.append(trello.boards.get(i))
            # cards.append(trello.boards.get(i).get('cards'))
            # organizations.append(user.organizations.get(i))
            # organizations.append(trello.organizations.get(i))
            # lists.append(trello.boards.get(i).get('lists').('name'))
        # for j in user.get('idOrganization'):
        #     organization.append(trello.organizations.get(j))
        return JsonResponse({'data': 'success', 'user': user, 'boards': boards, 'organizations': organizations, 'lists': lists, 'cards': cards})
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


def get_recent_events(request):
    http = httplib2.Http()
    http = client.OAuth2Credentials.from_json(request.session['credentials']).authorize(http)
    service = build('calendar', 'v3', http=http)
    request = service.events().list(calendarId='primary')

    data = []
    # Loop until all pages have been processed.
    while request is not None:
        # Get the next page.
        response = request.execute()
        # Accessing the response like a dict object with an 'items' key
        # returns a list of item objects (events).
        for event in response.get('items', []):
            # The event object is a dict object with a 'summary' key.
            data.append(event)
        # Get the next request object by passing the previous request object to
        # the list_next method.
        request = service.events().list_next(request, response)

        # Return the string of calendar data.
    return JsonResponse({'data': data})
