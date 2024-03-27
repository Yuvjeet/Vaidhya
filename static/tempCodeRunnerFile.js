function extract(string_data){
    var data = []
    var flag = false
    var str = ""
    console.log(string_data)
    for(let i in string_data){
        if(string_data[i] === "'"){
            flag = !flag
            if(str != ""){
                data.push(str)
                str = ""
            }
            continue
        }
        if(flag){
            console.log(i)
            str += i
        }
    }
    return data
}