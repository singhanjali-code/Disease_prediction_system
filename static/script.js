async function predict() {
    // Get all checked symptoms
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    const symptoms = Array.from(checkboxes).map(cb => cb.value);

    // Check if symptoms selected
    if (symptoms.length === 0) {
        alert('Please select at least one symptom!');
        return;
    }

    // Show loading
    document.querySelector('button').textContent = 'Predicting...';

    try {
        // Send to Flask API
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ symptoms: symptoms })
        });

        const data = await response.json();

        if (data.status === 'success') {
            // Show result
            document.getElementById('disease-name')
            .textContent = '🦠 ' + data.disease;
            
            document.getElementById('confidence')
            .textContent = 'Confidence: ' + data.confidence + '%';
            
            // Show result div
            document.getElementById('result')
            .classList.remove('hidden');
        }

    } catch (error) {
        alert('Error: ' + error.message);
    }

    // Reset button
    document.querySelector('button').textContent = 'Predict Disease';
}