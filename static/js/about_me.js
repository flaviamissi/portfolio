$(function() {
    $.get( "/api/about", function( data ) {
        $( "#about .experience" ).html( data.experience );
        $( "#about .passions" ).html( data.passions );
    });
});
