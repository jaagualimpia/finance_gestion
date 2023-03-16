const date = JSON.parse(document.getElementById('date').textContent);
const balance = JSON.parse(document.getElementById('balance').textContent);

console.log(date)
console.log(balance)

const ctx = document.getElementById('myChart');
new Chart(ctx, {
  type: 'line',
  data: {
    labels: date,
    datasets: [{
      label: 'Balance',
      data: balance,
      fill: true,
      borderColor: 'rgb(202, 5, 0)',
      borderWidth: 1
    }]
  },

  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true
      }
    }
    
  }
});

const ctx2 = document.getElementById('myChart2');
new Chart(ctx2, {
    type: 'bar',
    data: {
      labels: date,
      datasets: [{
        label: 'Balance',
        data: balance,
        fill: true,
        borderColor: 'rgb(75, 252, 252)',
        borderWidth: 1
      }]
    },
  
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true
        }
      }
      
    }
  });