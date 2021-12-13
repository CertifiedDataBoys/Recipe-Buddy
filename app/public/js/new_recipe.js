var ingredientsHTML = "";
var glob_ingredients = [];

$(document).ready(function() {
    // Initialize recipe name and subtitle selector
    $.getJSON("/api/v1.0.0./public/recipe/get_random?quantity=1", function(data) {
        $("#recipeName").attr("placeholder", data.recipes[0].title);
        $("#recipeSubtitle").attr("placeholder", data.recipes[0].subtitle);
    });

    // Initialize description
    tinymce.init({
        selector: '#recipeDescription',
        body_id: 'post-content-editor',
        toolbar: 'bold italic underline emoticons link image media table',
        plugins: 'emoticons image, table, link, imagetools, media',
        toolbar_mode: 'floating',
        menubar: false,
        branding: false
    });

    // Initialize kitchenware
    $.getJSON("/api/v1.0.0/public/food/get_all_kitchenware", function(data) {
        for (let i = 0; i < data.kitchenware.length; i++) {
            $("#kitchenware").append("<input type='checkbox' id='recipeKitchenware" + data.kitchenware[i].name.replace(/\s/g, '') + "' name='recipeKitchenware' value='" + data.kitchenware[i].name + "'> " + data.kitchenware[i].name + "<br>");
        }
    });

    // Initialize ingredients
    $.getJSON("/api/v1.0.0/public/food/get_all_ingredients", function(data) {
        glob_ingredients = data.ingredients;
        $("#recipe-ingredient-units-1").val(data.ingredients[0].unit_of_measure);
        for (let i = 0; i < data.ingredients.length; i++) {
            ingredientsHTML += "<option value='" + data.ingredients[i].pk + "'>" + data.ingredients[i].name + "</option>";
        }
        $("#recipe-ingredient-ingredient-1").append(ingredientsHTML);
    });
});

function updateIngredient(ingredient_id) {
    const quantity = $("#recipe-ingredient-quantity-" + ingredient_id)[0].value;
    const ingredient_pk = $("#recipe-ingredient-ingredient-" + ingredient_id)[0].value;
    var units;
    for (var i = 0; i < glob_ingredients.length; i++) {
        if (glob_ingredients[i].pk == ingredient_pk)
            units = (quantity <= 1) ? glob_ingredients[i].unit_of_measure : glob_ingredients[i].units_plural;
    }
    $("#recipe-ingredient-units-" + ingredient_id)[0].value = units;
}

var count = {
    media: 1,
    ingredient: 1,
    instruction: 1
}

function addMedia() {
    count.media++;
    var html = `
        <div class="recipe-media-div" id="recipe-media-` + count.media + `">
            <select id="recipeMediaType" class="form-control recipeMediaType">
                <option value="image">Image URL</option>
                <option value="video">YouTube Video URL</option>
            </select>
            <input type="text" class="form-control recipeMedia" placeholder="https://i.imgur.com/GbA4xZx.jpeg"><button onclick='$("#recipe-media-` + count.media + `").remove()'>X</button><br>
        </div>
        `;
    $("#recipeMediaSelector").append(html);
}

function addIngredient() {
    count.ingredient++;
    var html = `
            <div class="recipe-ingredient-div" id="recipe-ingredient-` + count.ingredient + `">
                <input type="number" value="1" class="recipe-ingredient-quantity" id="recipe-ingredient-quantity-` + count.ingredient + `" onchange="updateIngredient(` + count.ingredient + `);">
                <select class="recipe-ingredient-ingredient" id="recipe-ingredient-ingredient-` + count.ingredient + `" onchange="updateIngredient(` + count.ingredient + `);">
                    ` + ingredientsHTML + `
                </select>
                <input type="text" id="recipe-ingredient-units-` + count.ingredient + `" value="` + glob_ingredients[0].unit_of_measure + `" class="recipe-ingredient-units" readonly>
                <input type="checkbox" id="ingredient-` + count.ingredient + `-optional" class="recipe-ingredient-optional">Optional?<button onclick='$("#recipe-ingredient-` + count.ingredient + `").remove()'>X</button><br>
            </div>
        `;
    $("#recipeIngredientSelector").append(html);
}

function addInstruction() {
    count.instruction++;
    var html = `
            <div class="recipe-instruction-div" id="recipe-instruction-` + count.instruction + `">
                <input type="text" placeholder="Instruction ` + count.instruction + `" class="recipe-instruction form-control"><input type="checkbox" id="instruction-` + count.instruction + `-optional" class="recipe-instruction-optional"> Optional?<button class="btn" onclick='$("#recipe-instruction-` + count.instruction + `").remove()'>X</button><br>
            </div>
        `;
    $("#recipeInstructionSelector").append(html);
}

function youtubeGetId(url) {
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
    const match = url.match(regExp);

    return (match && match[2].length === 11) ?
        match[2] :
        null;
}

function isValidHttpUrl(string) {
    let url;

    try {
        url = new URL(string);
    } catch (_) {
        return false;
    }

    return url.protocol === "http:" || url.protocol === "https:";
}

function formValid() {
    var validity = {
        valid: true,
        msg: "",
        containsImg: false
    }
    if ($("#recipeName").val() == "") {
        validity.valid = false;
        validity.msg += "Recipe name cannot be empty.\n";
    }
    if ($("#recipeSubtitle").val() == "") {
        validity.valid = false;
        validity.msg += "Recipe subtitle cannot be empty.\n";
    }
    if (tinymce.get('recipeDescription').getContent({
            format: 'raw'
        }) == '') {
        validity.valid = false;
        validity.msg += "Recipe description cannot be empty.\n";
    }
    for (var i = 0; i < $(".recipe-ingredient-quantity").length; i++) {
        if ($($(".recipe-ingredient-quantity")[i]).val() == "") {
            validity.valid = false;
            validity.msg += "Ingredient(" + i + ") quantity cannot be empty.\n";
        }
        if ($($(".recipe-ingredient-ingredient")[i]).val() == "") {
            validity.valid = false;
            validity.msg += "Ingredient(" + i + ") ingredient cannot be empty.\n";
        }
        if ($($(".recipe-ingredient-units")[i]).val() == "") {
            validity.valid = false;
            validity.msg += "Ingredient(" + i + ") units cannot be empty.\n";
        }
    }
    for (var i = 0; i < $(".recipe-instruction").length; i++) {
        if ($($(".recipe-instruction")[i]).val() == "") {
            validity.valid = false;
            validity.msg += "Instruction(" + i + ") cannot be empty.\n";
        }
    }
    for (var i = 0; i < $(".recipeMedia").length; i++) {
        if ($($(".recipeMedia")[i]).val() == "") {
            validity.valid = false;
            validity.msg += "Media(" + i + ") cannot be empty.\n";
        }
        if ($(".recipeMediaType")[i].value == "image") {
            validity.containsImg = true;
            if (isValidHttpUrl($($(".recipeMedia")[i]).val()) == false) {
                validity.valid = false;
                validity.msg += "Media(" + i + ") must be a valid image URL.\n";
            }
        }
        if ($(".recipeMediaType")[i].value == "video") {
            if (!$(".recipeMedia")[i].value.includes("youtube.com") && !$(".recipeMedia")[i].value.includes("youtub.be")) {
                validity.valid = false;
                validity.msg += "Media(" + i + ") must be a valid YouTube URL.\n";
            }
        }
    }
    if (!validity.containsImg) {
        validity.valid = false;
        validity.msg += "Recipe must contain at least one image.\n";
    }
    return validity;
}

function submitRecipe() {
    var formValidity = formValid();
    if (formValidity.valid) {
        var recipe = {
            "title": $("#recipeName").val(),
            "subtitle": $("#recipeSubtitle").val(),
            "description": tinymce.get('recipeDescription').getContent({
                format: 'raw'
            }),
            "type": $("#recipeType").val(),
            "ingredients": [],
            "instructions": [],
            "media": []
        };

        for (var i = 0; i < $(".recipe-ingredient-quantity").length; i++) {
            var ingredient = {
                "count": $(".recipe-ingredient-quantity")[i].value,
                "name": $(".recipe-ingredient-ingredient")[i].value,
                "units": $(".recipe-ingredient-units")[i].value,
                "optional": $(".recipe-ingredient-optional")[i].checked
            };
            recipe.ingredients.push(ingredient);
        }

        for (var i = 0; i < $(".recipe-instruction").length; i++) {
            var instruction = {
                "description": $(".recipe-instruction")[i].value,
                "optional": $(".recipe-instruction-optional")[i].checked,
                "instruction_number": i + 1
            };
            recipe.instructions.push(instruction);
        }

        for (var i = 0; i < $(".recipeMedia").length; i++) {
            var media = {
                "is_video": $(".recipeMediaType")[i].value == "video",
                "media_link": $(".recipeMediaType")[i].value == "video" ? youtubeGetId($(".recipeMedia")[i].value) : $(".recipeMedia")[i].value
            };
            recipe.media.push(media);
        }

        recipe.is_private = $("#recipe-privacy").val() == 'private';

        $.ajax({
            url: "/api/v1.0.0/public/recipe/upload_recipe",
            type: "POST",
            data: JSON.stringify({
                recipe: recipe
            }),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(data) {
                window.location.href = "/recipe/" + data.recipe.pk;
            }
        });
    } else {
        alert(formValidity.msg);
    }
}