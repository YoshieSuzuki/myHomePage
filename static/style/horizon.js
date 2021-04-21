$(function() {
	winW = $(window).width();
	spped = 3000;
	$('#content').hide()
	function move(){
		$('#horizon').css({
			left: winW / 2
		}).animate({
			left: 0,
			width: winW
		}, 1000, 'swing', setTimeout(function(){
			$('#content').hide().fadeIn(500);
			},1000)
		);
	}
	move();
});