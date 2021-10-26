$(document).ready(function() {
    $('#username').keyup(function() {
        const userLength = /^.{4,32}$/;
        const s = $('#username').val();

        if (userLength.test(s)) {
            $('#user-restriction-length').text("✓");
        } else {
            $('#user-restriction-length').text("•");
        }
    });
    $('#email').keyup(function() {
        const emailLength = /^.{1,64}$/;
        const validEmail = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/; // https://stackoverflow.com/a/46181/5871303
        const s = $('#email').val();

        if (emailLength.test(s)) {
            $('#email-restriction-length').text("✓");
        } else {
            $('#email-restriction-length').text("•");
        }

        if (validEmail.test(s)) {
            $('#email-restriction-valid').text("✓");
        } else {
            $('#email-restriction-valid').text("•");
        }
    });
    $('#confirm_email').keyup(function() {
        const s = $('#email').val();
        const confirm =  $('#confirm_email').val();
        if (s === confirm) {
            $('#email-confirm-match').text("✓");
        } else {
            $('#email-confirm-match').text("•");
        }
    });
    $('#password').keyup(function() {
        const pwdLength = /^.{8,}$/;
        const pwdUpper = /[A-Z]+/;
        const pwdLower = /[a-z]+/;
        const pwdNumber = /[0-9]+/;
        const pwdSpecial = /[!@#$%^&()'[\]"?+-/*={}.,;:_]+/;
        const s = $('#password').val();

        if (pwdLength.test(s)) {
            $('#pwd-restriction-length').text("✓");
        } else {
            $('#pwd-restriction-length').text("•");
        }
        if (pwdUpper.test(s) && pwdLower.test(s)) {
            $('#pwd-restriction-upperlower').text("✓");
        } else {
            $('#pwd-restriction-upperlower').text("•");
        }
        if (pwdNumber.test(s)) {
            $('#pwd-restriction-number').text("✓");
        } else {
            $('#pwd-restriction-number').text("•");
        }
        if (pwdSpecial.test(s)) {
            $('#pwd-restriction-special').text("✓");
        } else {
            $('#pwd-restriction-special').text("•");
        }
    });
    $('#confirm_password').keyup(function() {
        const s = $('#password').val();
        const confirm =  $('#confirm_password').val();
        if (s === confirm) {
            $('#pwd-confirm-match').text("✓");
        } else {
            $('#pwd-confirm-match').text("•");
        }
    });
});
