$(function() {
    $.get( "/api/interests", function( data ) {
        data.forEach( function( item, index ) {
            $( "#interests .personal-interests" ).append("<li><b>" + item.title + "</b> " + item.description + "</li>");
        });
    });
});
