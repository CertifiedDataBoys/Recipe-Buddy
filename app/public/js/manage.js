var counts = {
    ingredients: 0,
    kitchenware: 0
}
var glob_ingredients = [];
var glob_kitchenware = [];

function addKitchenwareRow() {
    counts.kitchenware++;
    const randomKitchenware = (glob_ingredients.length == 0) ? {
        name: 'Wok'
    } : glob_kitchenware[Math.floor(Math.random() * glob_kitchenware.length)];

    const html = `
        <tr id="kitchenware-tr-` + counts.kitchenware + `">
            <td>
                <input type="text" class="form-control" id="kitchenware-name-` + counts.kitchenware + `" placeholder="` + randomKitchenware.name + `">
            </td>
            <td>
                <button class="btn btn-default" id="kitchenware-update-` + counts.kitchenware + `" onclick="updateKitchenware(` + counts.kitchenware + `, -1);">Submit</button>
            </td>
        </tr>
    `;
    $('#kitchenware-table').append(html);
}

function addIngredientRow() {
    counts.ingredients++;
    const randomIngredient = (glob_ingredients.length == 0) ? {
        name: "Lettuce 🥬",
        unit_of_measure: "leaf",
        units_plural: "leaves"
    } : glob_ingredients[Math.floor(Math.random() * glob_ingredients.length)];

    const html = `
                <tr id="ingredient-tr-` + counts.ingredients + `">
                    <td>
                        <input type="text" class="form-control" id="ingredient-name-` + counts.ingredients + `" placeholder="` + randomIngredient.name + `">
                    </td>
                    <td>
                        <input type="text" class="form-control" id="ingredient-unit-` + counts.ingredients + `" placeholder="` + randomIngredient.unit_of_measure + `">
                    </td>
                    <td>
                        <input type="text" class="form-control" id="ingredient-units-` + counts.ingredients + `" placeholder="` + randomIngredient.units_plural + `">
                    </td>
                    <td>
                        <button class="btn btn-default" id="ingredient-update-` + counts.ingredients + `" onclick="updateIngredient(` + counts.ingredients + `, -1);">Submit</button>
                    </td>
                </tr>
            `;
    $('#ingredients-table').append(html);
}

function updateKitchenware(count, pk) {
    const name = $('#kitchenware-name-' + count).val();
    const updateBtn = $('#kitchenware-update-' + count);

    if (pk == -1) {
        $.ajax({
            url: '/api/v1.0.0/public/food/create_kitchenware',
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify({
                name: name
            }),
            success: function(data) {
                if (data.success)
                    updateBtn.text(updateBtn.text() + " ✓");
                else
                    alert("Unable to create kitchenware: " + data.error);
            }
        });
    } else {
        $.ajax({
            url: '/api/v1.0.0/public/food/update_kitchenware?pk=' + pk,
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify({
                name: name
            }),
            success: function(data) {
                if (data.success)
                    updateBtn.text(updateBtn.text() + " ✓");
                else
                    alert("Unable to update kitchenware: " + data.error);
            }
        });
    }
}

function updateIngredient(count, pk) {
    const name = $('#ingredient-name-' + count).val();
    const unit = $('#ingredient-unit-' + count).val();
    const units = $('#ingredient-units-' + count).val();
    const updateBtn = $('#ingredient-update-' + count);

    if (pk == -1) {
        $.ajax({
            url: '/api/v1.0.0/public/food/create_ingredient',
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify({
                name: name,
                unit_of_measure: unit,
                units_plural: units
            }),
            success: function(data) {
                if (data.success)
                    updateBtn.text(updateBtn.text() + " ✓");
                else
                    alert("Unable to create ingredient: " + data.error);
            }
        });
    } else {
        $.ajax({
            url: '/api/v1.0.0/public/food/update_ingredient?pk=' + pk,
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify({
                name: name,
                unit_of_measure: unit,
                units_plural: units
            }),
            success: function(data) {
                if (data.success)
                    updateBtn.text(updateBtn.text() + " ✓");
                else
                    alert("Unable to update ingredient: " + data.error);
            }
        });
    }
}

$(document).ready(function() {
    $.getJSON("/api/v1.0.0/public/food/get_all_ingredients", function(data) {
        glob_ingredients = data.ingredients;
        var ingredientsHTML = '<table id="ingredients-table"><tr><th>Name</th><th>Unit</th><th>Units Plural</th><th>Actions</th></tr>';
        for (var i = 0; i < data.ingredients.length; i++) {
            counts.ingredients++;
            ingredientsHTML += `
                <tr id="ingredient-tr-` + counts.ingredients + `">
                    <td>
                        <input type="text" class="form-control" id="ingredient-name-` + counts.ingredients + `" value="` + data.ingredients[i].name + `">
                    </td>
                    <td>
                        <input type="text" class="form-control" id="ingredient-unit-` + counts.ingredients + `" value="` + data.ingredients[i].unit_of_measure + `">
                    </td>
                    <td>
                        <input type="text" class="form-control" id="ingredient-units-` + counts.ingredients + `" value="` + data.ingredients[i].units_plural + `">
                    </td>
                    <td>
                        <button class="btn btn-default" id="ingredient-update-` + counts.ingredients + `" onclick="updateIngredient(` + counts.ingredients + `, ` + data.ingredients[i].pk + `);">Update</button>
                    </td>
                </tr>
            `;
        }
        $('#ingredients-div').html(ingredientsHTML);
    });
    $.getJSON("/api/v1.0.0/public/food/get_all_kitchenware", function(data) {
        glob_kitchenware = data.kitchenware;
        var kitchenwareHTML = '<table id="kitchenware-table"><tr><th>Name</th><th>Actions</th></tr>';
        for (var i = 0; i < data.kitchenware.length; i++) {
            counts.kitchenware++;
            kitchenwareHTML += `
                <tr id="kitchenware-tr-` + counts.kitchenware + `">
                    <td>
                        <input type="text" class="form-control" id="kitchenware-name-` + counts.kitchenware + `" value="` + data.kitchenware[i].name + `">
                    </td>
                    <td>
                        <button class="btn btn-default" id="kitchenware-update-` + counts.kitchenware + `" onclick="updateKitchenware(` + counts.kitchenware + `, ` + data.kitchenware[i].pk + `);">Update</button>
                    </td>
                </tr>
            `;
        }
        $('#kitchenware-div').html(kitchenwareHTML);
    });
});