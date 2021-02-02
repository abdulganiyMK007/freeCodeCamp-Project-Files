// Github url: https://github.com/freeCodeCamp/boilerplate-project-headerparser.git

app.get("/api/whoami", (req, res) => {
	const language = req.header('Accept-Language')
	const software = req.header('User-Agent')
	const ipaddress = '127.0.0.1'

	res.json({ipaddress, language, software})
})









