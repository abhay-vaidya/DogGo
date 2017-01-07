(function($) {
    "use strict"; // Start of use strict

    //Click Function
    $("p").click(function(){
        $(this).hide();
    });

    //Hover function
    $("#p1").hover(function(){
        alert("You entered p1!");
    },
    function(){
        alert("Bye! You now leave p1!");
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