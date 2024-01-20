function calculateSum() {
    const num1 = document.getElementById("num1").value;
    const num2 = document.getElementById("num2").value;

    // Make an AJAX request to the backend
    fetch('/calculate_sum', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            num1: num1,
            num2: num2
        })
    })
        .then(response => response.json())
        .then(data => {
            // Display the result on the page
            document.getElementById("result").innerText = `Sum: ${data.result}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
