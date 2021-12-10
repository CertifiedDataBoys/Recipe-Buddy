$(document).ready(function() {
    $.getJSON('/api/v1.0.0/public/recipe/get_single_recipe_details?pk=' + window.location.pathname.split("/").pop(), function(data) {
        if (typeof data.error !== "undefined" && data.error) {
            $('#recipe-body').html('<p>' + data.message + '</p>');
        } else {
            $.each(data.recipe, function(key, val) {
                switch (key) {
                    case 'title':
                        $('#recipe_title').html(val);
                        $('#recipe_title_top').html(val);
                        $(document).attr('title', $(document).find("title").text() + ' - ' + val);
                        break;
                    case 'subtitle':
                        $('#recipe_subtitle').html(val);
                        break;
                    case 'description':
                        $('#recipe_description').html(val);
                        break;
                    case 'type':
                        $('#recipe_type').html("Type: <b>" + val + "</b>");
                        break;
                    case 'user':
                        $('#username').html(val.username);
                        break;
                    case 'uploaded':
                        $('#uploaded').html(val);
                        break;
                    case 'ingredients':
                        $.each(val, function(i, ingredient) {
                            const op = ingredient.optional ? " (Optional) " : "";
                            if (ingredient.count > 0)
                                $('#ingredients').append('<i>' + ingredient.count + ' ' + ingredient.unit + '</i> ' + ingredient.name + op + '<br/>');
                            else
                                $('#ingredients').append(ingredient.name + op + '<br/>');
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
                        break;
                    case 'media':
                        $.each(val, function(i, media) {
                            if (media.is_video) {
                                $('#media-container').append('<div class="col-sm-7"><iframe style="display: block;border-style:none;" width="420" height="315" src="https://www.youtube.com/embed/' + media.media_link + '"></iframe></div>');
                            } else {
                                $('#media-container').append('<div class="col-sm-7"><img class="img-fluid" src="' + media.media_link + '"></div>');
                            }
                        });
                        break;
                }
            });
        }
    });
});