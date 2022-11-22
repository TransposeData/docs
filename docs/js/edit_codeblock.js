function readCodeblock(event) {
	return event.target.parentElement.previousSibling.previousSibling.getElementsByTagName("code")[0].innerText;
}
