from api.models import Account
from django.http import JsonResponse
from frontend_views.views import flow


def store_trello_token(request):
    token = request.POST['token']

    a = Account.objects.get(user_id=request.user.id)
    a.trello_token = token
    a.save()
    return JsonResponse({'token': token})


def google_auth_callback(request):
    auth_code = request.GET.get('code')
    credentials = flow.step2_exchange(auth_code)
    request.session['credentials'] = credentials.to_json()
    return JsonResponse({'status': 'success'})
