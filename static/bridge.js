// var tag = document.getElementById("result");
var tag = document.getElementById("symptoms");
var greeting = document.getElementById("Diseases");
// var tags = document.getElementById("Tags");
var return_data = "";
function extract(string_data){
    var data = []
    var flag = false
    var str = ""
    for(let i = 0; i < string_data.length; i++){
        if(string_data[i] === "'"){
            flag = !flag
            if(str != ""){
                data.push(str)
                str = ""
            }
            continue
        }
        if(flag){
            str += string_data[i]
        }
    }
    return data
}
function generateTable(data){
    console.log(data)
    // div = document.createElement("div")
    // div.setAttribute("class", "Greatings")
    // p = document.createElement("p")
    // p.appendChild(document.createTextNode("Diseases You May Have: "))
    // div.appendChild(p)
    // tag.appendChild(div)
    tags.style.display = "none"
    greeting.style.display = "block"
    // tags.style.display = "block"
    var predictions = document.createElement("TABLE");
    predictions.setAttribute("id", "predictions");
    tag.appendChild(predictions);
    // var Thead = document.createElement("TH")
    // Thead.setAttribute("id", "Th")
    // predictions.appendChild(Thead)
    // Thead.appendChild(document.createTextNode("You May Have: "))
    for(var i in data){
        var row = document.createElement("TR");
        row.setAttribute("id", "Tr");
        predictions.appendChild(row);
        var row_data = document.createElement("TD");
        var disease = document.createTextNode(data[i]);
        row_data.appendChild(disease);
        row.appendChild(row_data);
    }
}
// function Search() {
//     var data = { "symptoms": getList()};
//     var return_data = ""
//     // console.log(data)
//     const request = new XMLHttpRequest();
//     request.open("POST", "/test");
//     request.setRequestHeader("Content-Type", "application/json");
//     request.onload = function() {
//         return_data = request.responseText
//     };
//     request.onerror = function() {
//         console.error("Request error");
//     };
//     request.send(JSON.stringify(data));
//     tag.innerHTML= "";
//     console.log(return_data);
//     generateTable(extract(return_data))

// }
function Search() {
    var data = { "symptoms": getList()};
    console.log(data)
    const request = new XMLHttpRequest();
    request.open("POST", "/test");
    request.setRequestHeader("Content-Type", "application/json");
    let return_data; // Declare return_data here
    request.onload = function() {
        tag.innerHTML= "";
        return_data = request.responseText
        console.log(return_data); // Log the response inside the onload function
        if(return_data === "'Normal'"){
            alert("Enter at least one symptom !");
            greeting.style.display = "none"
        }
        else generateTable(extract(return_data)); // Call the generateTable function inside the onload function
    };
    request.onerror = function() {
        console.error("Request error");
    };
    request.send(JSON.stringify(data));
}