let pollutantChart = null;
let indexChart = null;

async function getAQI() {
    const city = document.getElementById("cityInput").value;
    if (!city) return alert("Enter city");

    const res = await fetch(`/live-aqi?city=${city}`);
    const data = await res.json();

    document.getElementById("result").classList.remove("hidden");

    document.getElementById("cityName").innerText = data.city.toUpperCase();
    document.getElementById("aqiStatus").innerText =
        `Air Quality: ${data.prediction}`;

    document.getElementById("pm25").innerText = data.raw_values.pm2_5;
    document.getElementById("pm10").innerText = data.raw_values.pm10;
    document.getElementById("no2").innerText  = data.raw_values.no2;
    document.getElementById("so2").innerText  = data.raw_values.so2;

    setStatusColor(data.prediction);
    renderCharts(data);
}

function setStatusColor(status) {
    const box = document.getElementById("aqiStatus");
    box.className = "status";
    if (status === "Good") box.classList.add("good");
    else if (status === "Moderate") box.classList.add("moderate");
    else box.classList.add("bad");
}

function renderCharts(data) {
    if (pollutantChart) pollutantChart.destroy();
    if (indexChart) indexChart.destroy();

    pollutantChart = new Chart(pollutantChart = document.getElementById("pollutantChart"), {
        type: "bar",
        data: {
            labels: ["PM2.5", "PM10", "NO₂", "SO₂"],
            datasets: [{
                label: "µg/m³",
                data: [
                    data.raw_values.pm2_5,
                    data.raw_values.pm10,
                    data.raw_values.no2,
                    data.raw_values.so2
                ]
            }]
        }
    });

    indexChart = new Chart(document.getElementById("indexChart"), {
        type: "radar",
        data: {
            labels: ["SOi", "Noi", "Rpi", "SPMi"],
            datasets: [{
                label: "AQI Indices",
                data: [
                    data.indices.SOi,
                    data.indices.Noi,
                    data.indices.Rpi,
                    data.indices.SPMi
                ]
            }]
        }
    });

    fetch("/model-comparison")
        .then(res => res.json())
        .then(models => {
            new Chart(document.getElementById("modelChart"), {
                type: "bar",
                data: {
                    labels: Object.keys(models),
                    datasets: [{
                        label: "Accuracy",
                        data: Object.values(models)
                    }]
                }
            });
        });
}

function toggleTheme() {
    const body = document.body;
    const btn = document.getElementById("themeToggle");

    body.classList.toggle("dark");

    if (body.classList.contains("dark")) {
        btn.innerText = "☀️";
        localStorage.setItem("theme", "dark");
    } else {
        btn.innerText = "🌙";
        localStorage.setItem("theme", "light");
    }
}

// Persist theme + icon on reload
window.onload = () => {
    const savedTheme = localStorage.getItem("theme");
    const btn = document.getElementById("themeToggle");

    if (savedTheme === "dark") {
        document.body.classList.add("dark");
        btn.innerText = "☀️";
    } else {
        btn.innerText = "🌙";
    }
};

