const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const predictRoute = require('./routes/predict');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Routes
app.use('/predict', predictRoute);

// Default Route
app.get('/', (req, res) => {
  res.send('Fake News Detection API is Running!');
});

// Start Server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
