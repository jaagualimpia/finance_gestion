
function getData(number){
amount = document.getElementById(`amountId-${number}`).textContent
description = document.getElementById(`descriptionId-${number}`).textContent
date = document.getElementById(`dateId-${number}`).textContent
type = document.getElementById(`typeId-${number}`).textContent


document.getElementById('amountModal').innerText = 'Amount: ' + amount
document.getElementById('descriptionModal').innerText = 'Description: ' + description
document.getElementById('dateModal').innerText = 'Date: ' + date
document.getElementById('typeModal').innerText =  'type: ' + type


console.log(amount, description, date, transactionType)
}