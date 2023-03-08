function isPocketValidation(){
    specificPocket = document.getElementById('selectSpecificPocket')
    value = document.getElementById('selectIsPocket').value
    
    if(Boolean(value)){
        specificPocket.disabled = false
    }else{
        specificPocket.disabled = true
    }
}