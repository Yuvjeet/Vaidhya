// var input = document.getElementById("input")
// var symptoms = document.getElementById("symptoms")
// var tags = document.getElementById("tags")
// // console.log("working")

// function add_tags(){
//     console.log("running")
//     div = document.createElement("div")
//     p = document.createElement("p")
//     content = document.createTextNode(input.value);
//     p.appendChild(content)
//     div.appendChild(p)
//     symptoms.appendChild(div)
//     input.value = ""
//     tags.style.display = "block"
//     // symptoms.innerHTML += input.innerHTML
// }

// input.addEventListener("keypress", function(event){
//     // console.log("listen")
//     if(event.key === "Enter"){
//         console.log("function")
//         add_tags()
//     }
// })
var button = document.getElementById("btn")
var symp = document.getElementsByTagName("symptoms")
var data = symp.children("p")
button.click(function(){
    // $.ajax({
    //     url:'',
    //     type: 'get',
    //     contentType: 'application/json',
    //     data: {
    //         symptoms = 
    //     }
    // })
    for(var i = 0; i < data.length; i++){
        console.log(data[i].innerHTML)
    }
})

