hk = hk || {};

hk.HelloUserModel = BB.Model.extend({
    url: '/api/get_user_boards/',
    initialize: function () {
        this.fetch();
    }
});

hk.HelloView = BB.View.extend({
    el: '#hello',
    template: _.template($('#hello-template').html()),
    userTemplate: _.template($('#user-template').html()),

    initialize: function (options) {

        this.model = new hk.HelloUserModel();
        this.render();

        this.listenTo(this.model, 'sync', this.renderUser)
    },

    render: function () {
        this.$el.empty().append(this.template());
    },

    renderUser: function () {
        this.$('.user-holder').empty().append(this.userTemplate());
    },

    authSuccess: function () {
        __this = this
        $.ajax({
            type: 'POST',
            url: '/api/store_trello_token/',
            data: {
                token: Trello.token()
            },
            success: function (data) {
                helloView.model.fetch();
            }
        });
    },

    authFail: function () {
        alert('Authentication with Trello failed.')
    },

    events: {
        'click .trello-auth': 'trelloAuth',
        'click .google-auth': 'googleAuth',
        'click .google-test': 'googleTest'
    },

    trelloAuth: function () {
        _this = this;
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
        window.open(auth_uri);
    },

    googleTest: function () {
        $.ajax({
            type: 'POST',
            url: '/api/get_recent_events/',
            success: function (data) {
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
