$(document).ready(function(){
    
    $('#request-table div div > h2').hide();
    $('#request-table div div > h3').hide();
    $('#request-table div div > button').hide();
    
    $('#request-table div div').click(function(){
        $(this).children().slideToggle();
    });
    
});