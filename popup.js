var authenticationSuccess = function() { console.log(Successful authentication); };
var authenticationFailure = function() { console.log(Failed authentication); };


Trello.authorize({
  type: 'popup',
  name: 'Robin',
  scope: {
    read: 'true',
    write: 'true' },
  expiration: 'never',
  success: authenticationSuccess,
  error: authenticationFailure
});
