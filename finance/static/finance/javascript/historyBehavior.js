
function getData(number){
    amount = document.getElementById(`amountId-${number}`).textContent
    description = document.getElementById(`descriptionId-${number}`).textContent
    date = document.getElementById(`dateId-${number}`).textContent
    type = document.getElementById(`typeId-${number}`).textContent


    document.getElementById('amountModal').innerText = + amount
    document.getElementById('descriptionModal').innerText = 'Description: ' + description
    document.getElementById('dateModal').innerText = 'Date: ' + date
    document.getElementById('titleHeaderModal').innerText =  '' + type
    console.log(type);

        if (type == ' Egreso '){
            document.getElementById('titleHeaderModal').setAttribute('class', 'text-danger')
            document.getElementById('amountModal').setAttribute('class', 'text-danger')
        }else{
            document.getElementById('titleHeaderModal').setAttribute('class', 'text-success')
            document.getElementById('amountModal').setAttribute('class', 'text-success')
        }

    console.log(amount, description, date, type);
}