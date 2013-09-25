$(function(){
	$.get({
	  url: '{% url 'comments:fetch_comments'%}',
//	  url: '/comments/templates/comments/comments_template.html',

	  success: function(data) {
		$('div#comments').html(data)
	  }
 
	});
});