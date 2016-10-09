from __future__ import print_function

from api.models import Account
from django.http import JsonResponse

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

from oauth2client import client

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/calendar-python-quickstart.json
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Robin'

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

# def main():
#     """Shows basic usage of the Google Calendar API.
#
#     Creates a Google Calendar API service object and outputs a list of the next
#     10 events on the user's calendar.
#     """
#     credentials = get_credentials()
#     http = credentials.authorize(httplib2.Http())
#     service = discovery.build('calendar', 'v3', http=http)
#
#     now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
#     print('Getting the upcoming 10 events')
#     eventsResult = service.events().list(
#         calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
#         orderBy='startTime').execute()
#     events = eventsResult.get('items', [])
#
#     if not events:
#         print('No upcoming events found.')
#     for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         print(start, event['summary'])
#
#
# if __name__ == '__main__':
#     main()


import json

import flask
import requests

# def google_auth:
#     app = flask.Flask(__name__)
#
#     CLIENT_ID = '949315674402-adp43f1anpdi57ajb7liccbkfet1avjl.apps.googleusercontent.com'
#     CLIENT_SECRET = 'v3KITyms1tGgybWObOsKgFz1'  # Read from a file or environmental variable in a real app
#     SCOPE = 'https://www.googleapis.com/auth/calendar'
#     REDIRECT_URI = '/api/oauth2callback'
#
#
#     @app.route('/')
#     def index():
#       if 'credentials' not in flask.session:
#         return flask.redirect(flask.url_for('oauth2callback'))
#       credentials = json.loads(flask.session['credentials'])
#       if credentials['expires_in'] <= 0:
#         return flask.redirect(flask.url_for('oauth2callback'))
#       else:
#         headers = {'Authorization': 'Bearer {}'.format(credentials['access_token'])}
#         req_uri = 'https://www.googleapis.com/calendar'
#         r = requests.get(req_uri, headers=headers)
#         return r.text
#
#
#     @app.route('/api/oauth2callback')
#     def oauth2callback():
#       if 'code' not in flask.request.args:
#         auth_uri = ('https://accounts.google.com/o/oauth2/v2/auth?response_type=code'
#                     '&client_id={}&redirect_uri={}&scope={}').format(CLIENT_ID, REDIRECT_URI, SCOPE)
#         return flask.redirect(auth_uri)
#       else:
#         auth_code = flask.request.args.get('code')
#         data = {'code': auth_code,
#                 'client_id': CLIENT_ID,
#                 'client_secret': CLIENT_SECRET,
#                 'redirect_uri': REDIRECT_URI,
#                 'grant_type': 'authorization_code'}
#         r = requests.post('https://www.googleapis.com/oauth2/v4/token', data=data)
#         flask.session['credentials'] = r.text
#         return flask.redirect(flask.url_for('index'))
#
#
#     if __name__ == '__main__':
#       import uuid
#       app.secret_key = str(uuid.uuid4())
#       app.debug = False
#       app.run()






def store_trello_token(request):
    token = request.POST['token']

    a = Account.objects.get(user_id=request.user.id)
    a.trello_token = token
    a.save()

    return JsonResponse({'token': token})

def store_google_info(request):
    credentials = get_credentials()
    return JsonResponse({'data': 'success'})
