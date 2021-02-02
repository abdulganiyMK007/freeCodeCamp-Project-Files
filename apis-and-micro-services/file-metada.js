// Github url: https://github.com/freeCodeCamp/boilerplate-project-filemetadata.git

// Add to package.json, under dependency => "multer": "^1.4.2"


const multer = require('multer')
const upload = multer({dest: 'uploads/'})


app.post("/api/fileanalyse", upload.single('upfile'), (req, res) => {
	const {originalname: name, mimetype: type, size} = req.file

	res.json({name, type, size})
})



