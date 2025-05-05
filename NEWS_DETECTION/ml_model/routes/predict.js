const express = require('express');
const router = express.Router();
const { spawn } = require('child_process');
const path = require('path');

router.post('/', (req, res) => {
    const userInput = req.body.news;

    if (!userInput || userInput.trim() === '') {
        return res.status(400).json({ error: 'Input text is required.' });
    }

    const pythonScriptPath = path.join(__dirname, '..', 'python', 'predictor.py');
    const python = spawn('python', [pythonScriptPath, userInput]);

    let result = '';
    let errorOutput = '';

    python.stdout.on('data', (data) => {
        result += data.toString();
    });

    python.stderr.on('data', (data) => {
        errorOutput += data.toString();
    });

    python.on('close', (code) => {
        if (code !== 0 || errorOutput) {
            console.error(`Error: ${errorOutput}`);
            return res.status(500).json({ error: 'Prediction error', details: errorOutput });
        }

        res.json({ prediction: result.trim() });
    });
});

module.exports = router;
