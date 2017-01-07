(function($) {
    "use strict"; // Start of use strict

    var obj = jQuery.parseJSON( '{ "name": "John" }' );
	alert( obj.name === "John" );

    //Click Function
    $("p").click(function(){
        $(this).hide();
    });

    //Click function for remove button
    $(".remove").click(function(){
        $(this).hide();
    });

    //Click function for done button
    $(".done").click(function(){
        $(this).hide();
    });





})(jQuery); // End of use strict