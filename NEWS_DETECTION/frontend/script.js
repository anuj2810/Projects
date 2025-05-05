function predictNews() {
    const news = document.getElementById('newsInput').value;

    if (news.trim() === "") {
        alert("Please enter some text!");
        return;
    }

    // Display loading text
    document.getElementById('result').innerText = "Predicting... Please wait!";

    fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ news: news }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = ` ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = "Something went wrong! Please try again.";
    });
}
