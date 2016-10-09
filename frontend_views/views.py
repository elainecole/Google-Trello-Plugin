from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from api.models import Account
import json


def base_view(request):
    if not request.user.is_authenticated():
        return TemplateResponse(request, 'login.html', {})
    account = Account.objects.get(user_id=request.user.id)

    return TemplateResponse(request, 'hello.html', {'user': json.dumps(account.id)})
