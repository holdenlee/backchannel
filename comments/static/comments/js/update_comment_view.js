
	function fetch_comments(x) {
			$.ajax({
			  url: "{% url 'comments:fetch_comments' x %}",
//	  url: '/comments/templates/comments/comments_template.html',
			  success: function(data) {
				$('div#comments').html(data)
			  	}
			});
	}


$(document).ready(function() {
	$('#start_from').blur(function() {
		var x=parseInt($(this).val());
		fetch_comments(x);
	});
});