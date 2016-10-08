hk = hk || {};

hk.HelloView = BB.View.extend({
    el: '#hello',
    template: _.template($('#hello-template').html()),

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
                alert('Thanks for authenticating with Trello, your token is: ' + data.token);
            }
        });
    },

    authFail: function () {
        alert('Authentication with Trello failed.')
    },

    events: {
        'click .trello-auth': 'trelloAuth',
        'click .google-auth': 'googleAuth',

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
        $.ajax({
            type: 'POST',
            url: '/api/get_user_boards/'
        });
    }
});
