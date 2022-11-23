function updateAPIKey(newKey) {
	var codeStrings = document.getElementsByClassName('cm-string');
	console.log(codeStrings)
	for (var i = 0; i < codeStrings.length; i++) {
		var codeString = codeStrings[i];
		console.log(codeString.innerHTML);
		if (codeString.innerHTML === "'&lt;YOUR API KEY&gt;'" ) {
			console.log('found it');
			codeString.innerHTML = "'" + newKey + "'";
		}
	}
}
