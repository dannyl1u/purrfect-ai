const express = require('express');
const app = express();
const PORT = 8080;

const axios = require('axios');

app.use( express.json())

app.listen(
    PORT,
) 

app.get('/', (req, res) => {
    console.log("test")
    res.send("Hello")
})


app.get('/translate', async (req, res) => {
    var name = req.query.name
    console.log(name)

    // call the flask api
    try {
        const response = await axios.get(`https://translation-server.onrender.com/translate?name=${name}`);
        console.log(response.data);
        res.send(response.data);
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
})
