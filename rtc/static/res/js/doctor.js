$(document).ready(function(){
    
    var ankur = 0;
    
    $('.ankur-02').hide();
    $('.ankur-03').hide();
    $('.ankur-04').hide();
    $('.ankur-05').hide();

    $('.ankur-data').hide();

    $('.ankur-click').click(function(){
        $(this).next().slideToggle();
    });


    $('#content > div').hide();
        $('#content > div:nth-child(1)').show();
    
    
    $('#leftSideBar > div > a:nth-child(1)').click(function(){
        $('#leftSideBar > div > a').removeClass('active');
        $('#content > div').hide();
        $('#leftSideBar > div > a:nth-child(1)').addClass('active');
        $('#content > div:nth-child(1)').show();
    });
    
    
    $('#leftSideBar > div > a:nth-child(2)').click(function(){
        $('#leftSideBar > div > a').removeClass('active');
        $('#content > div').hide();
        $('#leftSideBar > div > a:nth-child(2)').addClass('active');
        $('#content > div:nth-child(2)').show();
    });
    
    
    $('#leftSideBar > div > a:nth-child(3)').click(function(){
        $('#leftSideBar > div > a').removeClass('active');
        $('#content > div').hide();
        $('#leftSideBar > div > a:nth-child(3)').addClass('active');
        $('#content > div:nth-child(3)').show();
    });
    
    
    $('#leftSideBar > div > a:nth-child(4)').click(function(){
        $('#leftSideBar > div > a').removeClass('active');
        $('#content > div').hide();
        $('#leftSideBar > div > a:nth-child(4)').addClass('active');
        $('#content > div:nth-child(4)').show();
    });
    
    
    $('#leftSideBar > div > a:nth-child(5)').click(function(){
        $('#leftSideBar > div > a').removeClass('active');
        $('#content > div').hide();
        $('#leftSideBar > div > a:nth-child(5)').addClass('active');
        $('#content > div:nth-child(5)').show();
    });
    
    
    $('#addMore').click(function(){
        if ( ankur == 0 ){
            $('.ankur-02').show();
            ankur++;
        }
        else if ( ankur == 1 ){
            $('.ankur-03').show();
            ankur++;
        }
        else if ( ankur == 2 ){
            $('.ankur-04').show();
            ankur++;
        }
        else if ( ankur == 3 ){
            $('.ankur-05').show();
            $('#addMore').hide();
        }
    });
    
    
});