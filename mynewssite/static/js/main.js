$(document).ready(function () {

    let progress_bar = $('.progress-bar')

    $('#id_password1').keyup(
        function (e) {
            let progress = $('#id_password1').val().length
            if (progress === 0) {
                progress_bar.addClass('w-0')
                progress_bar.setAttribute('aria-valuenow', '0')
            } else if (progress === 2) {
                progress_bar.addClass('w-25')
                progress_bar.setAttribute('aria-valuenow', '25')
            } else if (progress === 4) {
                progress_bar.addClass('w-50')
                progress_bar.setAttribute('aria-valuenow', '50')
            } else if (progress === 6) {
                progress_bar.addClass('w-75')
                progress_bar.setAttribute('aria-valuenow', '75')
            } else if (progress >= 9) {
                progress_bar.addClass('w-100')
                progress_bar.setAttribute('aria-valuenow', '100')
            }


        })
    $('#id_password2').keyup(
        function (e) {
            if ($('#id_password2').val() != $('#id_password1').val()) {
                $('#password_alert').show()

            } else {
                $('#password_alert').hide()
            }


        }
    )

    let button = $('#submitreg')
    $('#id_username').keyup(
        function (e) {
            $.post(
                '',
                {
                    'user': $('#id_username').val()
                },
                function (response) {
                    if (response.message) {
                        $('#login_alert').show();

                        button.addClass('disabled')
                        button.setAttribute('aria-disabled', 'true')
                    } else if (response.message === false) {
                        $('#login_alert').hide()
                        button.removeClass('disabled')
                        button.removeAttr('aria-disabled')
                    }
                }
            )
        }
    )
})


$(function () {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});