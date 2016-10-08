// Elaine Cole—Robin

var oauth = ChromeExOAuth.initBackgroundPage({
    'request_url' : 'https://www.google.com/accounts/OAuthGetRequestToken',
    'authorize_url' : 'https://www.google.com/accounts/OAuthAuthorizeToken',
    'access_url' : 'https://www.google.com/accounts/OAuthGetAccessToken',
    'consumer_key' : 'anonymous',
    'consumer_secret' : 'anonymous',
    'scope' : 'http://www.google.com/m8/feeds/',
    'app_name' : 'Robin'
});

var events = null;

function setIcon() {
    chrome.browserAction.setIcon({'path' : 'image/robin.png'});
};

function onEvents(text, xhr) {
    events = [];
    var data = JSON.parse(text);
    for (var i = 0, entry; entry = data.feed.entry[i]; i++) {
        var events = {
            'title' : entry['title']['$t'],
            'id' : entry['id']['$t']
        };
    }
};

function getEvents() {
	  oauth.authorize(function() {
	    console.log("on authorize");
	    setIcon();
	    var url = "https://www.googleapis.com/auth/calendar/default/full";
	    oauth.sendSignedRequest(url, onContacts, {
	      'parameters' : {
	        'alt' : 'json',
	        'max-results' : 100
	      }
	    });
	  });
	};

	function logout() {
	  oauth.clearTokens();
	  setIcon();
	};

	setIcon();
	chrome.browserAction.onClicked.addListener(getEvents);
