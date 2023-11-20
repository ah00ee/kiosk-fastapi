function updateQuantity(){
    const end = location.href.lastIndexOf("/");
    const start = location.href.substring(0, end).lastIndexOf("/");
    const place_id = location.href.substring(start+1, end);

    const menus = document.getElementsByClassName("menu");
    var index = 0;
    for(let i=0; i<menus.length; i++){
        if(menus[i].value !== ""){
            let parent = menus[i].parentNode.parentNode.parentNode;
            var name = parent.getElementsByClassName("menu-name")[i].innerText;
            var quantity = menus[i].value
            menus[i].value = null
        }
    }
    var url = `/user/place/${place_id}/manage`;
    fetch(url,{
        method: "PUT",
        header:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
                name: name,
                quantity: quantity
            })
        }
    );
}