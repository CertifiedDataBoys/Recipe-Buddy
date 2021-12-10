var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
    return false;
};
$(document).ready(function() {
    // Kitchenware Filters
    $.getJSON("/api/v1.0.0/public/food/get_all_kitchenware", function(data) {
        for (let i = 0; i < data.kitchenware.length; i++) {
            const html = `
                    <span id="sideBarKitchenwareFilter-` + i + `" class="sideBarButton" onclick="toggleKitchenwareFilter($('#sideBarKitchenwareFilter-` + i + `'));">` + data.kitchenware[i].name.replace(/\s/g, '') + `</span>
                `;
            $("#kitchenwareContainer").append(html);
        }
    });
    // Search page
    if (getUrlParameter("q")) {
        var query = getUrlParameter("q");
        if (getUrlParameter("q").length > 512) {
            $("#search-limit").html("<i>Your search query was limited to 512 characters</i> (Characters after \"" + query.substring(502, 512) + "\" were ignored)");
            query = getUrlParameter("q").substring(0, 512);
        }
        $("#recipe-search").val(query);
        $("#search-term").html(query);
        $.getJSON("/api/v1.0.0/public/recipe/search_recipes?q=" + query, function(data) {
            var recipes = Object.values(data.recipes);
            console.log(recipes[0]);
            recipes.sort(function(a, b) {
                return a["score"] < b["score"];
            });
            console.log(recipes);
            var html = "";
            for (var i = 0; i < recipes.length; i++) {
                html += "<div class='col-md-4'><div class='card'><div class='card-body' style='background: linear-gradient(to right, #fcba03, #fc9003);'><h5 class='card-title' style='color: black;'>" + recipes[i].recipe.title + "</h5><p class='card-text' style='color: black;'>" + recipes[i].recipe.subtitle + "</p><a href='/recipe/" + recipes[i].recipe.pk + "' class='btn search-btn'>View Recipe</a><p class='card-text' style='color: black;'>Relevance score: <i>" + recipes[i].score + "</i></p></div></div></div>";
            }
            $("#search-results").html(html);
        });
    }
});