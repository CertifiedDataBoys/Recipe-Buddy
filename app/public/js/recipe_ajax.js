$(document).ready(function() {
    $.getJSON('/api/v1.0.0/public/recipe/get_single_recipe_details?pk=' + window.location.pathname.split("/").pop(), function(data) {
        if (typeof data.error !== "undefined" && data.error) {
            $('#recipe-body').html('<p>' + data.message + '</p>');
        } else {
            $.each(data.recipe, function(key, val) {
                switch (key) {
                    case 'title':
                        $('#recipe_title').html(val);
                        $(document).attr('title', $(document).find("title").text() + ' - ' + val);
                        break;
                    case 'user':
                        $('#username').html(val.username);
                        break;
                    case 'uploaded':
                        $('#uploaded').html(val);
                        break;
                    case 'ingredients':
                        $.each(val, function(i, ingredient) {
                            if (ingredient.count > 0)
                                $('#ingredients').append('<i>' + ingredient.count + ' ' + ingredient.unit + '</i> ' + ingredient.name + '<br/>');
                            else
                                $('#ingredients').append(ingredient.name + ' (Optional)<br/>');
                        });
                        break;
                    case 'instructions':
                        $.each(val, function(i, instruction) {
                            $('#instructions').append('&nbsp;&nbsp;&nbsp;<strong>' + instruction.instruction_number + '.</strong> ' + instruction.description + (instruction.optional ? '(Optional)' : '') + '<br/>');
                        });
                        break;
                    case 'comments':
                        $.each(val, function(i, comment) {
                            // Is this comment a reply?
                            if (comment.reply_to != undefined) {
                                // Build a replies div if it doesn't exist
                                if ($('#comment-' + comment.reply_to + '-replies').length == 0) {
                                    $('#comment-' + comment.reply_to).append('<div class="border-left border-dark pl-4" id="comment-' + comment.reply_to + '-replies"></div>');
                                }
                                $('#comment-' + comment.reply_to + '-replies').append('<div id="comment-' + comment.pk + '"><div id = "comment-' + comment.pk + '-username" style="font-weight: bold;"></div> <small>' + comment.uploaded + '</small><br><div id = "comment-' + comment.pk + '-contents" style="white-space: pre-wrap;"></div><br></div>');
                            }
                            // Is this comment a suggestion?
                            else if (comment.suggestion) {
                                $('#comments').append('<div id="comment-' + comment.pk + '"><div id = "comment-' + comment.pk + '-username" style="font-weight: bold;"></div> <small>' + comment.uploaded + '</small><br><p class="text-center mb-2 text-muted">SUGGESTION</p><div id = "comment-' + comment.pk + '-contents" style="white-space: pre-wrap;"></div><br></div>');
                            } else {
                                $('#comments').append('<div id="comment-' + comment.pk + '"><div id = "comment-' + comment.pk + '-username" style="font-weight: bold;"></div> <small>' + comment.uploaded + '</small><br><div id = "comment-' + comment.pk + '-contents" style="white-space: pre-wrap;"></div><br></div>');
                            }
                            // Display our username and comment contents
                            $(document.createTextNode(
                                comment.user.username
                            )).appendTo('#comment-' + comment.pk + '-username');
                            $(document.createTextNode(
                                comment.contents.replace(/\n\n\n+/g, '\n\n')
                                .trim()
                            )).appendTo('#comment-' + comment.pk + '-contents');
                        });
                }
            });
        }
    });
});