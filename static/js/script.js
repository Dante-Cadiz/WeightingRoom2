var right_height = $("#column-right").height()
var left_height = $("#column-left").height()


if (right_height < left_height) {
    $("#column-right").height($("#column-left").height());
} else {
    $("#column-left").height($("#column-right").height());
}

