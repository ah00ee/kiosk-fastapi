
function getPlaceId(){
    const end = location.href.lastIndexOf("/");
    const place_id = location.href.substring(end+1);
    alert(place_id);
    return place_id;
}