function updateAPIKey(newKey) {
	var codeStrings = document.getElementsByClassName('cm-string');
	console.log(codeStrings)
	for (var i = 0; i < codeStrings.length; i++) {
		var codeString = codeStrings[i];
		console.log(codeString.innerHTML);
		if (codeString.innerHTML === "'BtRVYj7dgnYUcr1gSSfWhmrTShIb8RBG'") {
			console.log('found it');
			codeString.innerHTML = "'" + newKey + "'";
		}
	}
}

function sub_api_key() {
	const textAreas = document.getElementsByClassName('transpose_demo');
	for (var i = 0; i < textAreas.length; i++) {
		var textArea = textAreas[i];
		var editor = CodeMirror.fromTextArea(textArea);
		editor.getDoc().setValue('reee');
	}
	console.log(textAreas);
	// var textArea = document.getElementById('myScript');
	// var editor = CodeMirror.fromTextArea(textArea);
	// editor.getDoc().setValue('var msg = "Hi";');
	// updateAPIKey('reee');
}
