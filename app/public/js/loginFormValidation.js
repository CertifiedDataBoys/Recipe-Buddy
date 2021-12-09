$(document).ready(function() {
    var tests = {
        user_restriction_length: false,
        email_restriction_length: false,
        email_restriction_valid: false,
        email_confirm_match: false,
        pwd_restriction_length: false,
        pwd_restriction_upperlower: false,
        pwd_restriction_number: false,
        pwd_restriction_special: false,
        pwd_confirm_match: false
    };

    function updateValid(id, test) {
        test ? ($('#' + id).text("✓"), $('#' + id + '-color').css('color', '#0be000')) : ($('#' + id).text("•"), $('#' + id + '-color').css('color', '#fc9003'));
        tests[id.replace(/-/g, "_")] = test;
        Object.values(tests).every(Boolean) ? $('#submit').removeAttr('disabled') : $('#submit').attr('disabled', 'disabled');
    }

    $('#username').keyup(function() {
        const userLength = /^.{4,32}$/;
        const s = $('#username').val();

        updateValid('user-restriction-length', userLength.test(s));
    });
    $('#email').keyup(function() {
        const emailLength = /^.{1,64}$/;
        const validEmail = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/; // https://stackoverflow.com/a/46181/5871303
        const s = $('#email').val();

        updateValid('email-restriction-length', emailLength.test(s));
        updateValid('email-restriction-valid', validEmail.test(s));
    });
    $('#confirm_email').keyup(function() {
        const s = $('#email').val();
        const confirm = $('#confirm_email').val();

        updateValid('email-confirm-match', (s === confirm && s !== ""));
    });
    $('#password').keyup(function() {
        const pwdLength = /^.{8,}$/;
        const pwdUpper = /[A-Z]+/;
        const pwdLower = /[a-z]+/;
        const pwdNumber = /[0-9]+/;
        const pwdSpecial = /[!@#$%^&()'[\]"?+-/*={}.,;:_]+/;
        const s = $('#password').val();

        updateValid('pwd-restriction-length', pwdLength.test(s));
        updateValid('pwd-restriction-upperlower', (pwdUpper.test(s) && pwdLower.test(s)));
        updateValid('pwd-restriction-number', pwdNumber.test(s));
        updateValid('pwd-restriction-special', pwdSpecial.test(s));
    });
    $('#confirm_password').keyup(function() {
        const s = $('#password').val();
        const confirm = $('#confirm_password').val();

        updateValid('pwd-confirm-match', (s === confirm && s !== ""));
    });

    setTimeout(function() {
        $('#username').trigger('keyup');
        $('#email').trigger('keyup');
        $('#confirm_email').trigger('keyup');
        $('#password').trigger('keyup');
        $('#confirm_password').trigger('keyup');
    }, 250);
});