var ipn;
var sid;
var ulg = 0;
var ult = 0;


//function to populate a dropdown menu with values
function popsites(){
	$.getJSON( "http://myURL/popsites/", function( data ) {
		//console.log(data);
		for(val in data){
		$('#sitelist').append('<option value="'+data[val][0]+'">'+data[val][0]+ ': '+data[val][1]+ "</option>");
		}
		});
		$('#mModal').modal({backdrop: 'static', keyboard:false});
		$('#mModal').modal('show');
}

//grab user inputted data and store as variables in the browser
function closeModal(){
	var ipn = $('#inputname').val();
	var sid = $('#sitelist').val();
	
	if ($('#sitelist').val() =='' || $('#inputname').val() ==''){
		alert('Please fill in the form');
	}
	else {
		$('#uname').html(ipn);
		$('#usite').html(sid);
		$('#mModal').modal('toggle');
	}
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
	
}

//get position of login
function showPosition(position) {
	ult = position.coords.latitude;
	ulg = position.coords.longitude;
}

//load external page on exit
function exitpage(){
	location.href='http://myURL/nbpd';
}

//main function to route app to input user data into a db
function increasec(bid){
	$('#mbike').on("touch", function(){alert('hi')});
    var value = parseInt(document.getElementById('C'+bid).value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('C'+bid).value = value;
	var ipn = $('#uname').html();
	var sid = $('#usite').html();
	//alert(ipn+sid);
	$.getJSON( "http://myURL/"+bid+"/"+sid+"/"+ipn+"/"+ult+"/"+ulg+"/", function(data) {
		//console.log(data);
	});
}