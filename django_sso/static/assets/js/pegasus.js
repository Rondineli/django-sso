$(function () {
    $('#consoleModal').on('hidden.bs.modal', function () {
        $("#consoleModal iframe").remove();
        var $iframe = $("<iframe />").attr({
            name: "iframeConsole",
            id: "iframeConsole"
        });
        $("#consoleOutput").append($iframe);
    });

    if (document.getElementById("id_epl")) {
        CodeMirror.fromTextArea(
            document.getElementById("id_epl"),
            {"theme": "monokai", "mode": {"name": "text/x-sql"}, "lineNumbers": true}
        );
    }
});
