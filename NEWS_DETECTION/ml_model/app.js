const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const predictRoute = require('./routes/predict');

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.use('/predict', predictRoute);  // Ye line zaroor honi chahiye

const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
