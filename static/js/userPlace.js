function moveToSelectPage(place_id){
    var url = `/user/place/${place_id}`;
    fetch(url
    ).then(response => response.text())
    .then(_ => {
        window.location.href = url;
    });
}

function moveToPlaceCreation(){
    var url = `/user/place/create`;
    fetch(url
    ).then(response => response.text())
    .then(_ => {
        window.location.href = url;
    });
}