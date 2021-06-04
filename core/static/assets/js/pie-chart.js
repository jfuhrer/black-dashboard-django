
// Global Options
Chart.defaults.global.defaultFontFamily = 'Poppins';
Chart.defaults.global.defaultFontColor = '#1d253b'; //blackblue

// pie chart in summary for current portfolio. embedded in DB column "summary"
let myChart = document.getElementById('current-allocation-pie');

if(myChart !== null) {
    myChart =  myChart.getContext('2d')
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
         titleFontSize: 30,
         bodyFontSize: 30,
         callbacks: {
              label: function (tooltipItems, data) {
                        var i = tooltipItems.index;
                        return data.labels[i] + ": " + data.datasets[0].data[i] + " CHF";
                    }
              }
       }
      }
    });
}

let toBeChart = document.getElementById('tobe-allocation-bar');
if(toBeChart !== null) {
    toBeChart = toBeChart.getContext('2d')
    // to be asset allocation Bar chart
    new Chart(toBeChart, {
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
          legend: {
            display: true,
            labels:{
                fontColor:'#1d253b',//blackblue
                fontSize:20,
            }
          },
          title: {
            display: false,
          },
           scales: {
            yAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'CHF',
                fontSize:20
              },
              ticks: {
                fontSize:17
              }
            }],
            xAxes: [{
              ticks: {
                fontSize:17
              }
            }]
         },
         tooltips: {
             enabled: true,
             titleFontSize: 20,
             bodyFontSize: 20,
       }
        }
    });
}

// Anlegerprofil - strategy comparison chart risk vs reward
let strategyComparisonChart = document.getElementById('strategy-comparison');
if(strategyComparisonChart !== null) {
    strategyComparisonChart = strategyComparisonChart.getContext('2d')
    // to be asset allocation Bar chart
    new Chart(strategyComparisonChart, {
        type: 'line',
        data: {
            labels: ['Investition', 'Wachstum', 'Korrektur', 'Erholung', 'Wachstum'],
            datasets: [
                {
                    fill: false,
                    label: "Festverzinslich",
                    borderColor: 'rgba(223, 184, 184)',
                    backgroundColor: 'rgba(223, 184, 184, 0.6)', // duskyPink
                    data: [
                      5000,
                      5200,
                      4800,
                      5100,
                      5500
                     ]
                },
                {
                    fill: false,
                    label: "Sicherheit",
                    borderColor: 'rgba(201, 192, 177)', // beige third
                    backgroundColor: 'rgba(201, 192, 177, 0.6)',
                    data: [
                      5000,
                      5700,
                      4500,
                      5300,
                      5900
                     ]
                },
                {
                    fill: false,
                    label: "Ausgewogen",
                    borderColor: 'rgba(88, 168, 168)', // softCyan
                    backgroundColor: 'rgba(88, 168, 168, 0.6)',
                    data: [
                      5000,
                      6200,
                      4000,
                      5700,
                      6700
                     ]
                },
                {
                    fill: false,
                    label: "Wachstum",
                    borderColor: 'rgba(145, 156, 130)',
                    backgroundColor: 'rgba(145, 156, 130, 0.6)', // olivegreen secondary
                    data: [
                      5000,
                      6600,
                      3300,
                      6000,
                      7600
                     ]
                },
                {
                    fill: false,
                    label: "Aktien",
                    borderColor: 'rgba(252, 190, 24)',
                    backgroundColor: 'rgba(252, 190, 24, 0.6)', // yellow
                    data: [
                      5000,
                      7000,
                      2900,
                      6700,
                      8400
                     ]
                }
            ]
        },
        options: {
          legend: {
            display: true,
            labels:{
                fontColor:'#1d253b',//blackblue
                fontSize:25,
            },
             onHover: function(e) {
                e.target.style.cursor = 'pointer';
            }
            },
             hover: {
                onHover: function(e) {
                 var point = this.getElementAtEvent(e);
                if (point.length) e.target.style.cursor = 'pointer';
                else e.target.style.cursor = 'default';
            }},
          title: {
            text: 'Hypothetische Kursentwicklung in unterschiedlichen Szenarien',
            display: false,
          },
           scales: {
            yAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'CHF',
                fontSize:25,
                padding: 10
              },
              ticks: {
                fontSize: 20
            }
            }],
             xAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'Kursentwicklung',
                fontSize:25,
                padding: 10
              },
              ticks: {
                fontSize: 23,
                }
            }]
         },
         tooltips: {
             enabled: true,
             titleFontSize: 30,
             bodyFontSize: 30,
       }
        }
    });

}

/*
// Anlegerprofil - strategy comparison chart risk vs reward
let riskBubbleChart = document.getElementById('riskBubbleChart');
if(riskBubbleChart !== null) {
    riskBubbleChart = riskBubbleChart.getContext('2d')
    // to be asset allocation Bar chart
    new Chart(riskBubbleChart, {
        type: 'bubble',
        data: {
                datasets: [{
                label: 'Relax',
                data: [{
                  x: 1,
                  y: 1,
                  r: 50
                }],
                backgroundColor: 'rgb(223, 184, 184)'
              },
              {
                label: 'Select',
                data: [{
                  x: 2,
                  y: 2,
                  r: 50
                }],
                backgroundColor: 'rgb(201, 192, 177)'
              },
              {
                label: 'Balance',
                data: [{
                  x: 3,
                  y: 3,
                  r: 50
                }],
                backgroundColor: 'rgb(88, 168, 168)'
              },{
                label: 'Ambition',
                data: [{
                  x: 4,
                  y: 4,
                  r: 50
                }],
                backgroundColor: 'rgb(145, 156, 130)'
              },
              {
                label: 'Focus',
                data: [{
                  x: 5,
                  y: 5,
                  r: 50
                }],
                backgroundColor: 'rgb(252, 190, 24)'
              }],
        options: {
          legend: { display: true },
          title: {
            display: false,
          },
          scales: {

          },
        }
      }
    });

} */
