

var dropdown = document.getElementById('flowerName-Select');
            
function listTopTen(){
    var comname = dropdown.options[dropdown.selectedIndex].value;
    console.log(comname)
    if(comname.length){
        url = "/top/"+comname;
        console.log(url)
        $.get(url,(data)=>{
            data.forEach(element => {
                $('#top-list').append("<li>"+element+"</li>")
            });
        })
    }
}

dropdown.onchange =()=>{
    listTopTen();
}

