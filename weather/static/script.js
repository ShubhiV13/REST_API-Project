// Get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.getElementById("weatherForm").addEventListener("submit", async function(e){
    e.preventDefault();

    let city = document.getElementById("city").value;
    let date = document.getElementById("date").value;
    let resultDiv = document.getElementById("result");

    if (!city || !date) {
        resultDiv.innerHTML = `<p style="color: red;">Please enter both city and date!</p>`;
        return;
    }

    // Show loading
    resultDiv.innerHTML = `<p>🌤 Fetching weather data...</p>`;

    try {
        let response = await fetch("/api/weather/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({ city: city, date: date }),
            credentials: "include"
        });

        if (response.status === 403 || response.status === 401) {
            resultDiv.innerHTML = `<p style="color: orange;">⏰ Session expired! <a href="/login/">Click here to login again</a></p>`;
            return;
        }

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        let data = await response.json();

        resultDiv.innerHTML = `
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 20px; 
                        border-radius: 10px; 
                        margin-top: 20px;
                        color: white;">
                <h3 style="margin-top: 0; color: white;"> Weather in ${data.city}</h3>
                <p><strong>📅 Date:</strong> ${data.date}</p>
                <p><strong>🌡 Temperature:</strong> ${data.temperature}°C</p>
                <p><strong>💧 Humidity:</strong> ${data.humidity}%</p>
                <p><strong>☁️ Condition:</strong> ${data.condition}</p>
            </div>
        `;
        
        // Clear form
        document.getElementById("city").value = "";
        document.getElementById("date").value = "";

    } catch (error) {
        console.error("Error:", error);
        resultDiv.innerHTML = `
            <div style="background: #f8d7da; 
                        padding: 15px; 
                        border-radius: 10px; 
                        margin-top: 20px;
                        color: #721c24;
                        border: 1px solid #f5c6cb;">
                <strong>❌ Error:</strong> ${error.message}<br>
                Please try again or <a href="/login/">login again</a>.
            </div>
        `;
    }
});