function getThisId(datum){
	var newUrl = "http://youtube.com/embed/"+datum+"?autoplay=1&allowFullScreen=true";
	return newUrl;
}
function changeThisId(datum){
	document.getElementById("ytplayer").setAttribute("src",getThisId(datum));
	document.getElementById("id_video").setAttribute("value",datum);
}
$(document).ready(function(){
	$(".tvid").click(function(){
		$("#overlay").show();
	})
	$(document).keyup(function(e){
		if (e.keyCode === 27){
			$("#overlay").hide();
			$("#ytplayer").attr("src","http://www.youtube.com/embed/");
			$("#addToFav").removeClass("hidden");
		};
	});
	$("#close").click(function(){
		$("#overlay").hide();
		$("#ytplayer").attr("src","http://www.youtube.com/embed/");
		$("#addToFav").removeClass("hidden");
	});
	$("#addToFav").submit(function(){
		$("#addToFav").addClass("hidden");
		$.post('/success/', $(this).serialize(), function(data){
			$.done(function(){
				$("#message").html("Added to favorites!");
			});
		});
		return false;
	})
})