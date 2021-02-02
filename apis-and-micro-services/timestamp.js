// Github url: https://github.com/freeCodeCamp/boilerplate-project-timestamp.git

app.get("api/timestamp/", (req, res) => {
	const date = new Date()
	res.json({
		unix: date.getTime(),
		utc: date.toUTCString()
	})
})

app.get("/api/timestamp/:date", (req, res) => {
	const {date} = req.params

	let rDate = new Date(date)

	if (rDate.toString() === 'Invalid Date') {
		rDate = new Date(parseInt(date))
	}

	if (rDate.toString() === 'Invalid Date') {
		return res.json({error: 'Invalid Date'})
	} else {
		return res.json({
			unix: rDate.getTime(),
			utc: rDate.toUTCString()
		})
	}
})

