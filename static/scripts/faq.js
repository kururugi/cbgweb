function getMargin(x){
	var a = $(x).attr("style");
	if (a){
		return parseInt(a.substring(a.search(/margin-left/)).split(":")[1].split("px;")[0])
	}else{
		return 0;
	}
}
$(document).ready(function(){
	$("#comment_reply_field_0_submit").click(function(){
				$.get("/faq/newreply",{text:$("#comment_reply_field_0_text").val(),author:"Anon",parent:0},
					function(data){
						alert("Reply successfully sent! : " + data);
						//Reload page
						window.location = "/faq";
					}
				);
			});
	$(".comment_reply").click(function(){
		var id = this.id.split("_")[2];
		if ($("#comment_reply_field_" + id).css("display") == "none"){
			$("#comment_reply_field_" + id).css({display:"block"});
			$("#comment_reply_field_"+id + "_submit").click(function(){
				$.get("/faq/newreply",{text:$("#comment_reply_field_" + id + "_text").val(),author:"Anon",parent:id},
					function(data){
						alert("Reply successfully sent! : " + data);
						//Reload page
						window.location = "/faq";
					}
				);
			});
		}else{
			$("#comment_reply_field_" + id).css({display:"none"});
		}
	});
	$(".comment_load").click(function(){
		var id = this.id.split("_")[2];
		var doing = false;
		var display = null;
		var opacity;
		var string_id = "comment_" + id;
		var margin = getMargin($("#comment_" + id));
		var children = $("#comments").children();
		for (var i = 0,len=children.length;i<len;i++){
			var child = children[i];
			if (child.id == string_id){
				doing = true;
			}else if (doing){
				if (getMargin(child) > margin){
					if (display == null){
						if ($(child).css("display") == "none"){
							display = "block";
							opacity = 1;
						}else{
							display = "none";
							opacity = 0;
						}
					}
					var local = child;
					$(local).animate({
						opacity:opacity,
						height:'toggle'
					},200,function(){
						$(this).css({display:display});
					});
				}else{
					break;
				}
			}
		}
	});
	$(".comment_upvote").click(function(){
		var id = this.id.split("_")[2];
		$.get("/faq/vote",{id:id,vote:1});
	});
});
