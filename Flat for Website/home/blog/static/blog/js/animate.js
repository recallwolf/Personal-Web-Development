$(document).ready(function(){
	$(".nav a[href='#about']").click(function(){
        $("html,body").animate({
		scrollTop:$(".pcover").offset().top},1000);
	});
	$(".nav a[href='#project']").click(function(){
        $("html,body").animate({
		scrollTop:$(".pcover2").offset().top},1000);
	});
	$(".nav a[href='#memorabilia']").click(function(){
        $("html,body").animate({
		scrollTop:$(".pcover3").offset().top},1000);
	});
	$(".nav a[href='#contact']").click(function(){
        $("html,body").animate({
		scrollTop:$(".pcover5").offset().top},1000);
	});
});











 