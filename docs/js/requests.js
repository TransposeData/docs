document.querySelectorAll('.run-query-button').forEach(item => {
  item.addEventListener('click', event => {
    console.log('yee');
  })
})

function issueRequest(event) {
  	console.log('yee');

	var myHeaders = new Headers();
	myHeaders.append("x-api-key", "FxKTp6MHpWQDaos8SRnSetdIZiUYLliS");
	myHeaders.append("Content-Type", "application/json");

	var raw = JSON.stringify({
		"sql": "SELECT timestamp::date AS date, COUNT(*) AS num_sales FROM ethereum.nft_sales AS sales WHERE sales.contract_address = '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB' GROUP BY date HAVING COUNT(*) > 0;"
	});

	var requestOptions = {
 		method: 'POST',
  		headers: myHeaders,
  		body: raw,
  		redirect: 'follow'
	};

	fetch("https://api.transpose.io/sql", requestOptions)
  		.then(response => response.text())
  		.then(result => event.target.parentElement.nextSibling.getElementsByTagName('pre')[0].getElementsByTagName('code')[0].innerHTML = result)
  		.catch(error => console.log('error', error));
}

