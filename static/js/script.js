$(document).ready(function() {
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

$(".edit-comment").click(function(e){
    var buttonClicked = e.target;
    var userCommentContainer = $(buttonClicked).parents(".user-comment");
    $(userCommentContainer).hide();
    var editFormContainer = $(userCommentContainer).siblings(".edit-user-comment-wrapper");
    editFormContainer.show();

    
});

$(".discard").click(function(e){
    var buttonClicked = e.target;
    var editFormContainer = $(buttonClicked).parents(".edit-user-comment-wrapper");
    editFormContainer.hide();
    var userCommentContainer = $(editFormContainer).siblings(".user-comment");
    $(userCommentContainer).hide();
    
});
});