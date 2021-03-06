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
});
