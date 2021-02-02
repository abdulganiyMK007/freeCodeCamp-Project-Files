require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser')
const cors = require('cors');
const dns = require('dns')
const urlparser = require('url')
const app = express();

// Basic Configuration
const port = process.env.PORT || 3000
mongoose.connect(process.env.DB_URI, {useNewUrlParser: true, 
useUnifiedTopology: true})

// console.log(mongoose.connection.readyState)
// 0 = disconnected, 1 = connected, 2 = connecting, 3 = disconnecting

const schema = new mongoose.Schema({url: String})
const Url = mongoose.mode('Url', schema)

app.use(bodyParser.urlencoded({extended: false}))
app.use(cors())

app.use('/public', express.static('$(process.cwd())/public'));

app.get('/', function(req, res) {
	res.sendFile(process.cwd() + '/views/index.html');
});



app.post('/api/shorturl/new', function(req, res) {
	const {bodyurl} = req.body
	
	dns.lookup(urlparser.parse(bodyurl).hostname, (error, address) => {
		if (!address) {
			return res.json({error: 'invalid URL'})
		} else {
			const url = new Url({url: bodyurl})
			url.save((err, data) => {
				res.json({
					original_url: data.url,
					short_url: data.id
				})
			})
    	}
	})
})


app.get('/api/shorturl/:id', (req, res) => {
	const {id} = req.params

	Url.findById(id, (err, data) => {
		if (!data) {
			return res.json({error: 'invalid URL'})
		} else {
			res.redirect(data.url)
		}
	})
})



app.listen(port, function() {
	console.log(`Listening on port ${port}`)
})

















