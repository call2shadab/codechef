var girlCon = document.getElementById("girls");
var btn = document.getElementById("btn");
btn.addEventListener("click", function() {
	var req = new XMLHttpRequest();
	req.open('GET', 'https://call2shadab.github.io/shacker/girls.json')
	req.onload = function() {
		var dat = JSON.parse(req.responseText);
		renderHTML(dat);
	};
	req.send();
	})

function renderHTML(data) {
	var htmlString = "";
	for (i=0; i<data.length; i++) {
		htmlString += "<p>" + data[i].name + " loves the " + data[i].fav_color + " and "+ data[i].fav_food + "</p>";
	}
	girlCon.insertAdjacentHTML('beforeend',htmlString);

}