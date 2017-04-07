$(document).ready(function(){ 
$(window).scroll(function(){
var move = $("div.move");  
var guidenav = $("#guidenav");  
var top = $(document).scrollTop();
var currentId = "";  
move.each(function(index, div){
let m = $(div);
if (top <= m.offset().top) {  
currentId= "#" + m.attr("id");
return false;
} 
else {  
return true;   
}  
});  
var currentLink = guidenav.find(".par-colorb");  
if (currentId && currentLink.attr("href") != currentId){ 
currentLink.removeClass("par-colorb");  
guidenav.find("[href='" + currentId + "']").addClass("par-colorb"); 
}
}); 
});


