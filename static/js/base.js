$(document).ready(function(){
    // Calculate if fixed footer is needed
    let height = $(document).height();
    let footer = $('#footer').outerHeight();
    let topOfFooter = height - footer;
    window.innerHeight;

    if (topOfFooter < window.innerHeight){
        $('#footer').addClass('fixed-bottom');
    }
});