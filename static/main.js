$(document).ready(function(){
	var imgw = $(".simg").width();
	console.log(imgw); 
	$(".simg").css("height", imgw); 


	$(window).resize(function(){
		var imgw = $(".simg").width();
		console.log(imgw); 
		$(".simg").css("height", imgw);


	})

	$(".simg").click(function(){
	 	$(this).toggleClass("fullSize")
	
	})

})

