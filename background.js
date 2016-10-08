// document.addEventListener('DOMContentLoaded', function() {
//     document.getElementById("TrelloAuth").addEventListener("click", function(){
                //

        // function clickHandler(e) {
        //     chrome.tabs.update({url: "https://trello.com/1/authorize?expiration=never&name=Robin&key=1c4e6885b9d06b44eff07db8fb63b45f"});
        //     window.close(); // Note: window.close(), not this.close()
        // }
        // document.addEventListener('DOMContentLoaded', function() {
        //     document.getElementById('TrelloAuth').addEventListener('click', clickHandler);
        // });

    // });
// });
document.getElementById('RobinAuth').onclick = function () {
    // var authenticationSuccess = function() { console.log("Successful authentication"); };
    // var authenticationFailure = function() { console.log("Failed authentication"); };
    console.log($);
    //
    // Trello.authorize({
    //   type: 'popup',
    //   name: 'Robin',
    //   scope: {
    //     read: 'true',
    //     write: 'true' },
    //   expiration: 'never',
    //   success: authenticationSuccess,
    //   error: authenticationFailure
    // });

    $.ajax({
        url: 'https://robin-app.herokuapp.com/auth/login/',
        data: {
            username: $('#username').val(),
            password: $('#password').val()
        },
        success: function () {
            window.open('https://robin-app.herokuapp.com/');
        }
    });
};
