function reloadFilters(buttonElemId) {
    buttonElem = $('#' + buttonElemId);
    if (buttonElem.hasClass('typeFilter') && buttonElem.hasClass('sideBarButtonActive')) {
        buttonElem.removeClass('sideBarButtonActive');
    } else if (buttonElem.hasClass('typeFilter')) {
        $('.typeFilter').removeClass('sideBarButtonActive');
        console.log(buttonElem.attr("class"));
        buttonElem.addClass('sideBarButtonActive');
        console.log(buttonElem.attr("class"));
    } else if (buttonElem.hasClass('kitchenwareFilter')) {
        buttonElem.hasClass('sideBarButtonActive') ? buttonElem.removeClass('sideBarButtonActive') : buttonElem.addClass('sideBarButtonActive');
    }
    var typeFilters = $(".typeFilter.sideBarButtonActive").data('filter-type');
    var kitchenwareFilters = [];
    $(".kitchenwareFilter.sideBarButtonActive").each(function() {
        kitchenwareFilters.push($(this).data('filter-kitchenware'));
    });
    typeof typeFilters == 'undefined' ? typeFilters = '' : typeFilters = typeFilters;
    typeof kitchenwareFilters == 'undefined' ? kitchenwareFilters = '' : kitchenwareFilters = kitchenwareFilters;
    loadRecipes(typeFilters, kitchenwareFilters)
}

function loadRecipes(typeFilters, kitchenwareFilters) {
    $.getJSON("/api/v1.0.0./public/recipe/get_random?quantity=4&typeFilter=" + encodeURIComponent(typeFilters) + "&kitchenwareFilters=" + encodeURIComponent(kitchenwareFilters.join(",")), function(data) {
        if (data.recipes.length == 0) {
            return $("#home-container").html("<h1>No recipes found</h1>");
        }
        var html = `
            <div class="row mt-4">
            <div class="col-lg-7 col-md-6 mt-4 mb-4">
            <h2>Trending</h2>
            <hr>
            </div>
            </div>
        `;
        if (data.recipes.length > 0) {
            html += `
            <div class="row mt-4">
                <div class="col-lg-4 col-md-6">
                    <div class="container-fluid">
                        <div class="row mt-4">
                            <div class="col-lg-10 col-md-10">
                                <div class="display-card card w-500 shadow-sm border-0" onclick="window.location.href = '/recipe/` + data.recipes[0].pk + `';">
                                    <img class="display-card-img card-img-top" id="recipe-image-trending-` + data.recipes[0].pk + `">
                                    <div class="card-body" id="recipe-body">
                                        <h4 class="card-title text-center" id="recipe_title">` + data.recipes[0].title + `</h4>
                                        <p class="text-center">` + data.recipes[0].subtitle + `</p>
                                    </div>
                                </div>`;

            if (data.recipes.length > 1) {
                html += `
                                <div class="display-card card w-500 shadow-sm border-0" onclick="window.location.href = '/recipe/` + data.recipes[1].pk + `';">
                                    <img class="display-card-img card-img-top" id="recipe-image-trending-` + data.recipes[1].pk + `">
                                    <div class="card-body" id="recipe-body">
                                        <h4 class="card-title text-center" id="recipe_title">` + data.recipes[1].title + `</h4>
                                        <p class="text-center">` + data.recipes[1].subtitle + `</p>
                                    </div>
                                </div>`;
            }
            html += `</div>
                        </div>
                    </div>
                </div>
                `;
        }
        if (data.recipes.length > 2) {
            html += `
                <div class="col-lg-4 col-md-6">
                    <div class="container-fluid">
                        <div class="row mt-4">
                            <div class="col-lg-10 col-md-10">
                                <div class="display-card card w-500 shadow-sm border-0" onclick="window.location.href = '/recipe/` + data.recipes[2].pk + `';">
                                    <img class="display-card-img card-img-top" id="recipe-image-trending-` + data.recipes[2].pk + `">
                                    <div class="card-body" id="recipe-body">
                                        <h4 class="card-title text-center" id="recipe_title">` + data.recipes[2].title + `</h4>
                                        <p class="text-center">` + data.recipes[2].subtitle + `</p>
                                    </div>
                                </div>`;

            if (data.recipes.length > 3) {
                html += `
                                <div class="display-card card w-500 shadow-sm border-0" onclick="window.location.href = '/recipe/` + data.recipes[3].pk + `';">
                                    <img class="display-card-img card-img-top" id="recipe-image-trending-` + data.recipes[3].pk + `">
                                    <div class="card-body" id="recipe-body">
                                        <h4 class="card-title text-center" id="recipe_title">` + data.recipes[3].title + `</h4>
                                        <p class="text-center">` + data.recipes[3].subtitle + `</p>
                                    </div>
                                </div>`;
            }
            html += `
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        }
        data.recipes.forEach(function(recipe) {
            $.getJSON("/api/v1.0.0/public/recipe/get_single_recipe_details?pk=" + recipe.pk, function(rdata) {
                for (var i = 0; i < rdata.recipe.media.length; i++) {
                    if (!rdata.recipe.media[i].is_video) {
                        $("#recipe-image-trending-" + recipe.pk).attr("src", rdata.recipe.media[i].media_link);
                        break;
                    }
                }
            });
        });
        return $("#home-container").html(html);
    });
}

$(document).ready(function() {
    // Kitchenware Filters
    $.getJSON("/api/v1.0.0/public/food/get_all_kitchenware", function(data) {
        for (let i = 0; i < data.kitchenware.length; i++) {
            const html = `
                <span id="sideBarKitchenwareFilter-` + i + `" class="sideBarButton kitchenwareFilter" data-filter-kitchenware="` + data.kitchenware[i].pk + `" onclick="reloadFilters(this.id);">` + data.kitchenware[i].name.replace(/\s/g, '') + `</span>
            `;
            $("#kitchenwareContainer").append(html);
        }
    });
    loadRecipes([], []);
});