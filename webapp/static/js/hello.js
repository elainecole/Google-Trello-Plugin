hk = hk || {};

hk.HelloView = BB.View.extend({
    el: '#hello',
    template: _.template($('#hello-template').html()),
    userTemplate: _.template($('#user-template').html()),

    initialize: function (options) {
        this.render();
    },

    render: function () {
        this.$el.empty().append(this.template());
    },

    authSuccess: function () {
        $.ajax({
            type: 'POST',
            url: '/api/store_trello_token/',
            data: {
                token: Trello.token()
            },
            success: function (data) {
                var me = Trello.members.get('me', function (user) {
                    alert('Thanks for authenticating with Trello, ' + user.fullName + '!');
                });
            }
        });
    },

    authFail: function () {
        alert('Authentication with Trello failed.')
    },
    // flow = client.flow_from_clientsecrets(
    //     'client_secrets.json',
    //     scope='https://www.googleapis.com/auth/calendar',
    //     redirect_uri='http://robin-app.herokuapp.com/api/store_google_info')
    //
    events: {
        'click .trello-auth': 'trelloAuth',
        'click .google-auth': 'googleAuth',
        'click .trello-test': 'trelloConnect'

    },

    trelloAuth: function () {
        Trello.authorize({
            type: 'popup',
            name: 'Robin',
            scope: {
            read: 'true',
            write: 'true' },
            expiration: 'never',
            success: this.authSuccess,
            error: this.authFail
        });
    },
    googleAuth: function () {
        // auth_uri = flow.step1_get_authorize_url()
        // window.open('https://accounts.google.com/o/oauth2/v2/auth?scope=email%20profile&state=security_token%3D138r5719ru3e1%26url%3Dhttps://oa2cb.example.com/myHome&redirect_uri=https%3A%2F%2Foauth2.example.com%2Fcode&,response_type=code&client_id=949315674402-adp43f1anpdi57ajb7liccbkfet1avjl.apps.googleusercontent.com')
        // $.ajax({
        //     type: 'POST',
        //     url: '/api/store_google_info/'
        // });
        // credentials = flow.step2_exchange(auth_code)
        $.ajax({
            type: 'POST',
            url: '/api/oauth2callback/',
            success: function(data) {
                debugger;
            }
        });

    },
    trelloConnect: function () {
        var _this = this;

        $.ajax({
            type: 'POST',
            url: '/api/get_user_boards/',
            success: function (data) {
                _this.$('.user-holder').empty().append(_this.userTemplate(data));
                // alert('Thank you ' + data.user.fullName);
            }
        });
    },
    // trelloBoards: function() {
    //     $.ajax({
    //         type: 'GET',
    //         url: '/1/members/' + data.userBoards.shortUrl'/boards'
    //     });
    // }
});
