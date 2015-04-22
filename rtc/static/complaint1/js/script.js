$(document).ready(function(){
	
	ankur = 0;
	
	$('#ankur tr:nth-child(5)').hide();	
	$('#ankur tr:nth-child(6)').hide();	
	$('#ankur tr:nth-child(7)').hide();	
	$('#ankur tr:nth-child(8)').hide();


	$('#addMore').click(function(){
		if ( ankur == 0 ){
			$('#ankur tr:nth-child(5)').show();
			ankur++;
		}
		else if ( ankur == 1 ){
			$('#ankur tr:nth-child(6)').show();
			ankur++;
		}
		else if ( ankur == 2 ){
			$('#ankur tr:nth-child(7)').show();
			ankur++;
		}
		else if ( ankur == 3 ){
			$('#ankur tr:nth-child(8)').show();
			$('#addMore').hide();
		}
	});
	
});