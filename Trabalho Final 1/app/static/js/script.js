$(document).ready(function() {
    // eventos de click dos botões que fazem a requisição na api do Flask
    $("#luz-sala").click(function() {
        $.post("evento/luz/sala", response);
    });

    $("#luz-quarto").click(function() {
        $.post("evento/luz/quarto", response);
    });

    $("#portao").click(function() {
        $.post("evento/portao", response);
    });
});

function response(data) {
    alert(data);
}