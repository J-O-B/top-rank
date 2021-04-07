$(document).ready(function(){
    $('#contain-edit').hide();
    $('#up').hide();
    $('#extra-controls').hide();
    $('#message-container').hide();
    $('#messenger').hide();
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
$('#open-messenger').click(function(){
    $('#messenger').show();
    $('html, body').animate({
        scrollTop: $('#messenger').offset().top - 20
    }, 'slow');
})

$(".message-box").click(function(){
    $('#initMessage').hide();
    let sentBy = $(this).find('.sender').text();
    let created = $(this).find('.created').text();
    let directMessage = $(this).find('.directMessage').text();
    $('#sent_by').text(`Sent From: ${sentBy}`);
    $('#created').text(`Sent On: ${created}`);
    $('#directMessage').text(`Message: ${directMessage}`);
})