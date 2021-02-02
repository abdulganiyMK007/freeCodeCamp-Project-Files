const express = require('express')
const app = express()
const bodyParser = require('body-parser')

const cors = require('cors')
const mongoose = require('mongoose')
new {Schema} =  mongoose
mongoose.connect(process.env.MONGO_URI || 'mongodb://localhost/exercise-track',
    {useNewUrlParser: true})


const personSchema = new mongoose.Schema({username: {type: String, unique: true}})
const Person = mongoose.mode('Person', personSchema)

const exerciseSchema = new mongoose.Schema({
    userId: String,
    description: String,
    duration: Number,
    date: Date
})
const Exercise = mongoose.mode('Exercise', exerciseSchema)


app.use(cors)

app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())


app.use(express.static('public'))
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/views/index.html')
});


app.post('/api/exercise/new-user', (req, res) => {

    const newPerson = new Person({username: req.body.username})
    newPerson.save((err, data) => {
        if (err) {
            res.json('Username already taken')
        } else {
            res.json({'username': data.username, '_id': data.id})
        }
    })
})


app.get('/api/exercise/users', (req, res) => {
	Person.find({}, (err, data) => {
        if (!data) {
            res.send('No users')
        } else {
            res.json(data)
        }
    })
})


app.post('/api/exercise/add', (req, res) => {
    const { userId, description, duration, date } = req.body
    
    if (!date) { date = new Date() }

    Person.findById(userId, (err, data) => {
        if (!data) {
            res.send('Unknown userid')
        } else {
            const username = data.username
            const newExercise = new Exercise({userId, description, duration, date})
            newExercise.save((err, data) => {
                res.json({
                    _id: userId,
                    username,
                    date: new Date(date).toDateString(),
                    duration: +duration,
                    description
                })
            })
        }
    })
})



app.get('/api/exercise/log', (req, res) => {
	const { userId, from, to, limit } = req.query
  
    Person.findById(userid, (err, data) => {
        if (!data) {
            res.send('Unknown userId')
        } else {
            const username = data.username
            Exercise.find({userId}, {date: {$gte: new Date(from), $lte: new Date(to)}})
            .select(['id', 'description', 'duration', 'date'])
            .limit(+limit).exec((err, data) => {

                let customdata = data.map(exer => {
                    let dateFormatted = new Date(exer.date).toDateString()
                    return {
                        id: exer.id, 
                        description: exer.description, 
                        duration: exer.duration, 
                        date: dateFormatted
                    }
                })

                if (!data) {
                    res.json({
                        'userId': userId,
                        'username': username,
                        'count': 0,
                        'log': []
                    })
                } else {
                    res.json({
                        'userId': userId,
                        'username': username,
                        'count': data.length,
                        'log': customdata
                    })
                }
            })
        }
    })
	
	
	
})

const listener = app.listen(process.env.PORT || 3000, () => {
  console.log('Your app is listening on port ' + listener.address().port)
})
