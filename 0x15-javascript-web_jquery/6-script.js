//Script that updates the text of the <header> element to the new
//Header when the user clicks on DIV#update_header

$('DIV#update_header').click(function () {
	$('header').html('New Header!!!');
});
