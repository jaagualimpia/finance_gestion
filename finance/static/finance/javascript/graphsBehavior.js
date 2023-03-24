const date = JSON.parse(document.getElementById('date').textContent);
const balance = JSON.parse(document.getElementById('balance').textContent);
const tendency = JSON.parse(document.getElementById('tendency').textContent);

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
    },

    {
      label: 'Prediction tendency',
      data: tendency,
      fill: true,
      borderColor: 'rgb(225, 223, 0)',
      borderWidth: 1
    }]
  },

  options: {
    responsive: true,
    scales: {
      y: {
        
      }
    }
    
  }
});