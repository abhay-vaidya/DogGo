(function ($) {
    "use strict"; // Start of use strict
    var input = {
        "name": "Kohilan"
        , "id": 1
        , "order_total": 12.00
        , "amount_paid": 0
        , "order": [
            {
                "name": "hot dog"
                , "type": "beef"
                , "count": 1
                , "price": 3.00
                , "combo": false
		}
            , {
                "name": "fries"
                , "count": 1
                , "price": 3.00
		}
	]
    , }
    var customerName = input.name;
    var id = input.id;
    var order_total = input.order_total;
    var amount_paid = input.amount_paid;
    var amount_due = order_total - amount_paid;
    var list_of_items = input.order;
    $("#customerName").html(customerName);
    $(".price").html("$" + amount_due);
    $("#orderNumber").html(id);
    var htmlItemsList = document.getElementById("listOfItems");
    //Loop through each order item
    for (var i = 0; i < list_of_items.length; i++) {
        var listItem = document.createElement("LI");
        htmlItemsList.appendChild(listItem);
        //        var itemName = $("<h2 class='itemName'></h2>").text(list_of_items[i].name);
        var itemName = document.createElement("H2");
        itemName.className += ' itemName';
        itemName.innerHTML = list_of_items[i].name;
        listItem.appendChild(itemName);
        console.log(listItem);
        //        $("listOfItems").append(listItem);
        //document.querySelector('#listOfItems').appendChild(list)
    }
    //Click Function
    $("p").click(function () {
        $(this).hide();
    });
    //Click function for remove button
    $(".remove").click(function () {
        $(this).hide();
    });
    //Click function for done button
    $(".done").click(function () {
        $(this).hide();
    });
})(jQuery); // End of use strict