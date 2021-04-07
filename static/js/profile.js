$(document).ready(function(){
    $('#contain-edit').hide();
    $('#up').hide();
    $('#extra-controls').hide();
    $('#message-container').hide();
});
$('#edit_my_profile').click(function(e){
    e.preventDefault();
    $('#contain-edit').siblings().hide();
    $('#contain-edit').show(1000);
});
$('#expand-controls').click(function(e){
    e.preventDefault();
    $('#up').toggle();
    $('#down').toggle();
    $('#extra-controls').toggle();
});
$('#show-messages').click(function(){
    $('#message-container').siblings().hide();
    $('#message-container').show();
});


// Messages
