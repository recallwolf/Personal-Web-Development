$("document").ready(function(){
	$(".ul1 a[href='#about']").click(function(){
        $("html,body").animate({
		scrollTop:$(".pcover").offset().top},1000);
	});
	$(".ul1 a[href='#project']").click(function(){
        $("html,body").animate({
		scrollTop:$(".pcover2").offset().top},1000);
	});
	$(".ul1 a[href='#memorabilia']").click(function(){
        $("html,body").animate({
		scrollTop:$(".pcover3").offset().top},1000);
	});
});











 