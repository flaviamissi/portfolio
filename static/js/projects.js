$(function() {
    $.get( "/api/projects", function( data ) {
        data.highlights.forEach( function( item, index ) {
            $( "#about .highlights" ).append("<li>" + item + "</li>");
        });

        data.recents.forEach( function( item, index ) {
            $( "#interests .recent-projects" ).append("<li>" + item + "</li>");
        });

        data.other.forEach( function( item, index ) {
            $( "#interests .other" ).append("<li>" + item + "</li>");
        });
    });

    $.get( "/api/interests", function( data ) {
        data.forEach( function( item, index ) {
            $( "#interests .personal-interests" ).append("<li><b>" + item.title + "</b>" + item.description + "</li>");
        });
    });
});
