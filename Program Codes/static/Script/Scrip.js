document.querySelector("h1.custname").style.backgroundColor = "pink";

function bulkCheck() {
    if (selected_quantity.options[selected_quantity.selectedIndex].text == "Bulk Order") {
        const label = document.createElement("label");
        label.setAttribute("for", "Quantitytext");
        label.innerHTML = "Type in the No. of Orders: ";
        label.setAttribute("id", "QuantityID");
        document.body.appendChild(label);

        const input = document.createElement("input");
        input.setAttribute("type", "text");
        input.setAttribute("id", "Quantitytext");
        document.body.appendChild(input);

        document.getElementById('bulkconfirm').disabled = true;
        document.getElementById("bulkconfirm").innerHTML = "Done!";
        document.getElementById("flag").innerHTML = "bulkbro";
    } else {
        document.getElementById("bulkconfirm").innerHTML = "Done!";
        document.getElementById("quantities").value =
            selected_quantity.options[selected_quantity.selectedIndex].text;
    }
    
    document.getElementById("name").value =
        selected_food.options[selected_food.selectedIndex].text;
};

let cow = '2';

function countbulk() {
    const selected_food = document.getElementById("movie");
    const selected_quantity = document.getElementById("Quantity");
    
    document.getElementById("name").value =
        selected_food.options[selected_food.selectedIndex].text;
    document.getElementById("quantities").value =
        selected_quantity.options[selected_quantity.selectedIndex].text;
    cow = selected_quantity.options[selected_quantity.selectedIndex].text;
}

function cowseat() {
    var selected_seat = document.getElementById("row");
    var selected_seatno = document.getElementById("seatno");

    document.getElementById("rownames").value =
        selected_seat.options[selected_seat.selectedIndex].text;
    document.getElementById("rownos").value =
        selected_seatno.options[selected_seatno.selectedIndex].text;

    if (cow == '2') {
        var selected_seat = document.getElementById("row2");
        var selected_seatno = document.getElementById("seat2no");

        document.getElementById("rownames2").value =
            selected_seat.options[selected_seat.selectedIndex].text;
        document.getElementById("rownos2").value =
            selected_seatno.options[selected_seatno.selectedIndex].text;
    }
    
    if (cow == '3') {
        var selected_seat = document.getElementById("row2");
        var selected_seatno = document.getElementById("seat2no");

        document.getElementById("rownames2").value =
            selected_seat.options[selected_seat.selectedIndex].text;
        document.getElementById("rownos2").value =
            selected_seatno.options[selected_seatno.selectedIndex].text;

        var selected_seat = document.getElementById("row3");
        var selected_seatno = document.getElementById("seat3no");

        document.getElementById("rownames3").value =
            selected_seat.options[selected_seat.selectedIndex].text;
        document.getElementById("rownos3").value =
            selected_seatno.options[selected_seatno.selectedIndex].text;
    }
    
    if (cow == '4') {
        var selected_seat = document.getElementById("row2");
        var selected_seatno = document.getElementById("seat2no");

        document.getElementById("rownames2").value =
            selected_seat.options[selected_seat.selectedIndex].text;
        document.getElementById("rownos2").value =
            selected_seatno.options[selected_seatno.selectedIndex].text;

        var selected_seat = document.getElementById("row3");
        var selected_seatno = document.getElementById("seat3no");

        document.getElementById("rownames3").value =
            selected_seat.options[selected_seat.selectedIndex].text;
        document.getElementById("rownos3").value =
            selected_seatno.options[selected_seatno.selectedIndex].text;

        var selected_seat = document.getElementById("row4");
        var selected_seatno = document.getElementById("seat4no");

        document.getElementById("rownames4").value =
            selected_seat.options[selected_seat.selectedIndex].text;
        document.getElementById("rownos4").value =
            selected_seatno.options[selected_seatno.selectedIndex].text;
    }

    if (cow == '5') {
        var selected_seat = document.getElementById("row2");
        var selected_seatno = document.getElementById("seat2no");

        document.getElementById("rownames2").value =
            selected_seat.options[selected_seat.selectedIndex].text;
        document.getElementById("rownos2").value =
            selected_seatno.options[selected_seatno.selectedIndex].text;

        var selected_seat = document.getElementById("row3");
        var selected_seatno = document.getElementById("seat3no");

        document.getElementById("rownames3").value =
            selected_seat.options[selected_seat.selectedIndex].text;
        document.getElementById("rownos3").value =
            selected_seatno.options[selected_seatno.selectedIndex].text;

        var selected_seat = document.getElementById("row4");
        var selected_seatno = document.getElementById("seat4no");

        document.getElementById("rownames4").value =
            selected_seat.options[selected_seat.selectedIndex].text;
        document.getElementById("rownos4").value =
            selected_seatno.options[selected_seatno.selectedIndex].text;

        var selected_seat = document.getElementById("row5");
        var selected_seatno = document.getElementById("seat5no");

        document.getElementById("rownames5").value =
            selected_seat.options[selected_seat.selectedIndex].text;
        document.getElementById("rownos5").value =
            selected_seatno.options[selected_seatno.selectedIndex].text;
    }
}

const selectElement = document.querySelector('.foood');
selectElement.addEventListener('change', () => {
    const result = document.querySelector('.Price');
    result.textContent = `${event.target.value}`;
});