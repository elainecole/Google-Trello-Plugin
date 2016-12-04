from django.template.response import TemplateResponse
from api.models import Account
import json
from oauth2client import client
import os

flow = client.flow_from_clientsecrets(
    os.getcwd() + '/api/client_secret.json',
    scope='https://www.googleapis.com/auth/calendar',
    redirect_uri='http://127.0.0.1:8000/api/google_auth_callback')


def base_view(request):
    if not request.user.is_authenticated():
        return TemplateResponse(request, 'login.html', {})
    account = Account.objects.get(user_id=request.user.id)

    auth_uri = flow.step1_get_authorize_url()

    return TemplateResponse(request, 'hello.html', {
        'user': json.dumps(account.id),
        'auth_uri': json.dumps(auth_uri)
    })
