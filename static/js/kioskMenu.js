function getMenu(){
    const menus = document.getElementsByClassName("menu");
    const table = document.getElementById("cart-table");

    for(let i=0; i<menus.length; i++){
        if(menus[i].value !== '' || menus[i].value!==0){
            let parent = menus[i].parentNode.parentNode.parentNode;
            var name = parent.getElementsByClassName("menu-name")[0].innerText;
            var price = parent.getElementsByClassName("menu-price")[0].innerText;
            var item = menus[i].value;

            const newRow = table.insertRow();
            const newNameCell = newRow.insertCell();
            const newQuantityCell = newRow.insertCell();
            const newPriceCell = newRow.insertCell();

            // className 지정
            newNameCell.className = 'name';
            newQuantityCell.className = 'quantity';
            newPriceCell.className = 'price';

            newNameCell.innerText = name;
            newQuantityCell.innerText = item;
            newPriceCell.innerText = price*item;

            menus[i].value = null;
        }
    }
}

function order(){
    const cart = document.getElementById("cart-table");
    const divs = cart.getElementsByTagName("tr");
    if(divs.length === 1){
        alert("결제할 상품이 없습니다.");
        return false
    }

    const end = location.href.lastIndexOf("/");
    const start = location.href.substring(0, end).lastIndexOf("/");
    const place_id = location.href.substring(start+1, end);

    var url = `/kiosk/place/${place_id}/order`;
    var menus = [];
    for(let i=1; i<divs.length; i++){
        var name = document.getElementsByClassName("name")[i-1].innerText;
        var quantity = document.getElementsByClassName("quantity")[i-1].innerText;
        var price = document.getElementsByClassName("price")[i-1].innerText;
        menus.push({
            menu_name: name,
            quantity: quantity,
            total_price: price
        })
    }
    fetch(url,{
        method: "POST",
        header:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            menus: menus
        }),
        redirect: 'manual'
        }
    ).then(response => response.text())
    .then(_ => {
        window.location.href = url;
    });
}