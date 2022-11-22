document.querySelectorAll('.run-query-button').forEach(item => {
  item.addEventListener('click', event => {
    console.log('yee');
  })
})

function issueRequest(event, sql_input_id, output_id) {
	var myHeaders = new Headers();
	myHeaders.append("x-api-key", "FxKTp6MHpWQDaos8SRnSetdIZiUYLliS");
	myHeaders.append("Content-Type", "application/json");

	var raw = JSON.stringify({
		"sql": document.getElementById(sql_input_id).getElementsByTagName("code")[0].innerText
	});

	var requestOptions = {
 		method: 'POST',
  		headers: myHeaders,
  		body: raw,
  		redirect: 'follow'
	};

	fetch("https://api.transpose.io/sql", requestOptions)
  		.then(response => response.text())
  		.then(result => document.getElementById(output_id).getElementsByTagName('code')[0].innerText = result)
  		.catch(error => console.log('error', error));
}

