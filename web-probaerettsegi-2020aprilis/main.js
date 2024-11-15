$(document).ready(function () {
  $('.navbar-nav li').click(function (x) {
    $('.navbar-nav li').removeClass('active');
    $(event.target).parent().addClass('active');
  });
});

function showCircuit() {
    $('#circuit').change(function (o) {
      switch (o.target.value) {
        case 'ITA':
          $('#circuitimage').attr('src', 'img/monza.jpg');
          $('#f1sound')[0].play();
          break;
        case 'HUN':
          $('#circuitimage').attr('src', 'img/hungaroring.jpg');
          break;
        case 'BEL':
          $('#circuitimage').attr('src', 'img/spa.jpg');
          break;
        case 'MON':
          $('#circuitimage').attr('src', 'img/monaco.jpg');
          break;

        default:
          break;
      }
    });
  }

//---------------------------------------------------------

function calculate() {
  const circuit = document.getElementById('circuit').value;
  const lapTime = parseFloat(document.getElementById('laptime').value);
  
  if (!circuit || isNaN(lapTime) || lapTime <= 0) {
      document.getElementById('averagespeed').value = '';
      return;
  }

  let circuitLength = 0;
  switch (circuit) {
      case 'HUN':
          circuitLength = 4.381;
          break;
      case 'MON':
          circuitLength = 3.337;
          break;
      case 'BEL':
          circuitLength = 7.004;
          break;
      case 'ITA':
          circuitLength = 5.793;
          break;
      default:
          return;
  }

  const averageSpeed = (circuitLength / (lapTime / 3600)).toFixed(2); 

  document.getElementById('averagespeed').value = averageSpeed + ' km/h';
}