$(document).ready(function() {
    {% if 'recipe' in page %}
    $.getJSON('/api/v1.0.0/public/recipe/get_single_recipe_details?pk={{pk}}', function(data) {
        $.each(data.recipe, function(key, val) {
            console.log(key);
            switch (key) {
                case 'title':
                    $('#recipe_title').html(val);
                    $(document).attr('title', 'Recipe - ' + val);
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
            }
        });
    });
    {% endif %}
});