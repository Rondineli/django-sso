function request_ajax_initial(url_request){
  var date = new Date();
  var month = date.getMonth() + 1;
  var year = date.getFullYear();
  $.get(url_request + month + '/' + year +'/?key=123456', function(data){
    $('#consolidation').html(data);
    changeIds();
    });
}
function changeIds(){
  var date = new Date();
  var next_month = date.getMonth() + 2;
  var previus_month = date.getMonth();
  var year = date.getFullYear();
  var previous_year = year;
  if (next_month == 13){
    year = year + 1
    next_month = 01
  }
  if (previus_month <= 0){
    previus_month = 12
    previous_year = year - 1;
  }
  first_day_of_month = new Date(date.getYear(), date.getMonth());
  last_day_of_month = new Date(date.getYear(), date.getMonth(), 0);

  $('#tablePanel').html("Referente ao mês "+ (
    date.getMonth() + 1) + "/" + date.getFullYear() + " Mostrando do dia: " + first_day_of_month.getUTCDate() + "a "+ last_day_of_month.getUTCDate()) ;

  $('#nextMonth').attr('id', next_month + '/' + year);
  $('#previusMonth').attr('id', previus_month + '/' + previous_year );
}
function getAjaxNextMonth(element, url_request){
  $.get(url_request + element.id +'/?key=123456', function(data){
    $('#consolidation').html(data);
    var next_month = Number(element.id.split('/')[0]);
    next_month = next_month + 1;
    next_year = Number(element.id.split('/')[1]);
    if (next_month == 13){
      next_month = 1;
      next_year = Number(element.id.split('/')[1]) + 1;
    }
    previus_month = Number(element.id.split('/')[0]) - 1;
    previus_year = Number(element.id.split('/')[1]);
    if (previus_month == 0){
      previus_month = 12;
      previus_year = previus_year - 1;
    }
    year = Number(element.id.split('/')[1]);

  $('#tablePanel').html("Referente ao mês "+ element.id + " Mostrando do dia:  1 a 31") ;
    $('#nextMonth').attr('id', next_month + '/' + next_year);
    $('#previusMonth').attr('id', previus_month + '/' + previus_year);  
  });
}
function getAjaxPreviusMonth(element, url_request){
  $.get(url_request + element.id +'/?key=123456', function(data){
    $('#consolidation').html(data);
    var next_month = Number(element.id.split('/')[0]);
    next_month = next_month + 1;
    next_year = Number(element.id.split('/')[1]);
    if (next_month == 13){
      next_month = 1;
      next_year = Number(element.id.split('/')[1]) + 1;
    }
    previus_month = Number(element.id.split('/')[0]) - 1;
    previus_year = Number(element.id.split('/')[1]);
    if (previus_month == 0){
      previus_month = 12;
      previus_year = previus_year - 1;
    }
    year = Number(element.id.split('/')[1]);
    $('#tablePanel').html("Referente ao mês "+ element.id + " Mostrando do dia:  1 a 31") ;
    $('#nextMonth').attr('id', next_month + '/' + next_year);
    $('#previusMonth').attr('id', previus_month + '/' + previus_year);
    });
}
