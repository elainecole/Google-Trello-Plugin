from django.conf.urls import url
import read, write

urlpatterns = [
    url(r'^store_trello_token/$', write.store_trello_token, name='store_trello_token'),
    url(r'^get_user_boards/$', read.get_user_boards, name='get_user_boards')
]
