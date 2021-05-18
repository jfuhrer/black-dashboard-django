// pie chart in summary for current portfolio. embedded in DB column "summary"
    let myChart = document.getElementById('current-allocation-pie').getContext('2d');

    // Global Options
    Chart.defaults.global.defaultFontFamily = 'Poppins';
    Chart.defaults.global.defaultFontSize = 17;
    Chart.defaults.global.defaultFontColor = '#1d253b'; //blackblue

    let massPopChart = new Chart(myChart, {
      type:'pie', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
      data:{
        labels:['Anleihen', 'Liquidität', 'Aktien', 'Alternative Anlagen'],
        tooltipText: ["Wild Quess", "Very Analytical", "Fine Prediction", "Bob's opinion"],
        datasets:[{
          label:'CHF',
          data:[
            5000,
            15000,
            18500,
            7000
          ],
          backgroundColor:[
            'rgba(223, 184, 184)', // duskyPink
            'rgba(145, 156, 130)', // olivegreen secondary
            'rgba(201, 192, 177)', // beige third
            'rgba(88, 168, 168)' // softCyan
          ],
          borderWidth:2,
          hoverBorderWidth:2,
          hoverBorderColor:'#ced4da' // light
        }]
      },
      options:{
        title:{
          display:false,
          text:'Aktuelle Verteilung Portfolio',
          fontSize:35
        },
        legend:{
          display:true,
          position:'right',
          labels:{
            fontColor:'#1d253b',//blackblue
            fontSize:30,
          }
        },
        layout:{
          padding:{
            left:0,
            right:0,
            bottom:0,
            top:10
          }
        },
       tooltips: {
        enabled: true,
         callbacks: {
             label: function (tooltipItems, data) {
                        var i = tooltipItems.index;
                        return data.labels[i] + ": " + data.datasets[0].data[i] + " CHF";
                    }
              }
       }
      }
    });

/*
 // Current asset allocation Bar chart
new Chart(document.getElementById("current-allocation-bar").getContext('2d'), {
    type: 'bar',
    data: {
      labels: ['Anleihen', 'Liquidität', 'Aktien', 'Alternative Anlagen'],
      datasets: [
        {
          label: "CHF",
          backgroundColor: [
            'rgba(223, 184, 184)', // duskyPink
            'rgba(145, 156, 130)', // olivegreen secondary
            'rgba(201, 192, 177)', // beige third
            'rgba(88, 168, 168)' // softCyan
            ],
          data:[
            5000,
            15000,
            18500,
            7000
          ],
          }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'IST Verteilung'
      },
       scales: {
        yAxes: [{
          scaleLabel: {
            display: true,
            labelString: 'CHF',
            fontSize:20
          }
        }]
     }
    }
});*/


 // to be asset allocation Bar chart
new Chart(document.getElementById("tobe-allocation-bar").getContext('2d'), {
    type: 'bar',
    data: {
        labels: ['Anleihen', 'Liquidität', 'Aktien', 'Alternative Anlagen'],
        datasets: [
            {
                label: "IST",
                backgroundColor: 'rgba(223, 184, 184)', // duskyPink,
                data: [
                  5000,
                  15000,
                  18500,
                  7000
                 ]
            },
            {
                label: "SOLL",
                backgroundColor: 'rgba(145, 156, 130)', // olivegreen secondary
                data: [
                  3000,
                  10000,
                  23500,
                  10000
                 ]
                    }
        ]
    },
    options: {
      legend: { display: true },
      title: {
        display: false,
      },
       scales: {
        yAxes: [{
          scaleLabel: {
            display: true,
            labelString: 'CHF',
            fontSize:20
          }
        }]
     }
    }
});
