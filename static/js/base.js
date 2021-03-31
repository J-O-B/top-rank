$(document).ready(function(){
    // Calculate if fixed footer is needed
    let height = $(document).height();
    let footer = $('#footer').outerHeight();
    let extra = height + footer;
    
    /*if ((height + footer) < window.innerHeight){
        //$('#footer').addClass('fixed-bottom');
    }else {
        $('#footer').removeClass('fixed-bottom');
    }
    if (window.innerWidth < 992){
        $('#footer').removeClass('fixed-bottom');
    }*/
    // Logo image loaded - if error, display title text
    $("#topLogo")
        .on('load', function() { 
            // Loaded Successfully 
        })
        .on('error', function() { 
            $(this).hide();
            $('#titleText').removeClass('hidden');
        });
});