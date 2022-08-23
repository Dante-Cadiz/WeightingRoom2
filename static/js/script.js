var right_height = $("#column-right").height()
var left_height = $("#column-left").height()


if (right_height < left_height) {
    $("#column-right").height($("#column-left").height());
} else {
    $("#column-left").height($("#column-right").height());
}


setTimeout(function () {
    let messages = $('.message');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 5000);

$(".edit-comment").click(function(){
    $("#edit-form").toggle();
});