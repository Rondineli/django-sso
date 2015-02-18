$(function () {
    $('#consoleModal').on('hidden.bs.modal', function () {
        $("#consoleModal iframe").remove();
        var $iframe = $("<iframe />").attr({
            name: "iframeConsole",
            id: "iframeConsole"
        });
        $("#consoleOutput").append($iframe);
        $("#formConsole").show();
    });

    $("#formConsole").submit(function() {
       $("#formConsole").toggle(500); 
    });

    if (document.getElementById("id_epl")) {
        CodeMirror.fromTextArea(document.getElementById("id_epl"), {"theme": "monokai", "mode": {"name": "text/x-sql"}, "lineNumbers": true});
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            }
        }
  });

});
