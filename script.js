
const city = document.querySelector("#city")
const btn = document.querySelector("#getWeather")
const result = document.querySelector("#result")
const cityNameElement = document.querySelector("#cityName")
const weatherDescription = document.querySelector("#weatherDescription")
const temperature = document.querySelector("#temperature")
const feelsLike = document.querySelector("#feelsLike")
const humidity = document.querySelector("#humidity")
const wind = document.querySelector("#wind")
const error = document.querySelector("#error")
const weatherIcon = document.querySelector("#weatherIcon")
const forecastDays = document.querySelector("#forecastDays")

function getWeather() {
    const cityName = city.value.trim()

    if (cityName === "") {
        error.textContent = "Enter a city"
        return
    }

    error.textContent = ""
    btn.textContent = "Loading..."
    btn.disabled = true

    fetch(`http://127.0.0.1:8000/weather?city=${encodeURIComponent(cityName)}`)
        .then((response) => {
            if (!response.ok) {
                throw new Error("City not found or server error")
            }
            return response.json()
        })
        .then((data) => {
            console.log(data)

            error.textContent = ""

            cityNameElement.textContent = `Weather in ${cityName}`

            temperature.textContent =
                `Temperature right now is: ${data.current.temperature_2m} ${data.current_units.temperature_2m}`

            feelsLike.textContent =
                `Feels like: ${data.current.apparent_temperature} ${data.current_units.apparent_temperature}`

            humidity.textContent =
                `Humidity: ${data.current.relative_humidity_2m} ${data.current_units.relative_humidity_2m}`

            wind.textContent =
                `Wind speed: ${data.current.wind_speed_10m} ${data.current_units.wind_speed_10m}`

            weatherDescription.textContent = data.weather_description

            const weatherCode = data.current.weather_code
            let icon = "🌡️"

            if (weatherCode === 0) {
                icon = "☀️"
            } else if (weatherCode <= 3) {
                icon = "🌤️"
            } else if (weatherCode === 45 || weatherCode === 48) {
                icon = "🌫️"
            } else if (weatherCode >= 51 && weatherCode <= 67) {
                icon = "🌧️"
            } else if (weatherCode >= 71 && weatherCode <= 77) {
                icon = "❄️"
            } else if (weatherCode >= 80 && weatherCode <= 82) {
                icon = "🌦️"
            } else if (weatherCode >= 95 && weatherCode <= 99) {
                icon = "⛈️"
            }
            console.log(data.daily)
            console.log(data.daily.time)
            console.log(data.daily.temperature_2m_max)
            forecastDays.innerHTML = ""
            for (let i = 0; i < data.daily.time.length; i++) {
            const card = document.createElement("div")
                const code = data.daily.weather_code[i]
                let forecastIcon = "🌡️"

                if (code === 0) {
                    forecastIcon = "☀️"
                } else if (code <= 3) {
                    forecastIcon = "🌤️"
                } else if (code === 45 || code === 48) {
                    forecastIcon = "🌫️"
                } else if (code >= 51 && code <= 67) {
                    forecastIcon = "🌧️"
                } else if (code >= 71 && code <= 77) {
                    forecastIcon = "❄️"
                } else if (code >= 80 && code <= 82) {
                    forecastIcon = "🌦️"
                } else if (code >= 95) {
                    forecastIcon = "⛈️"
                }

            card.classList.add("forecast-card")
                const date = new Date(data.daily.time[i] + "T12:00:00")

                const formattedDate = date.toLocaleDateString("en-US", {
                    weekday: "short",
                    month: "short",
                    day: "numeric"
                })

            card.innerHTML = `
                <h3>${formattedDate}</h3>
                <div class="forecast-icon">${forecastIcon}</div>
                <p>Max: ${data.daily.temperature_2m_max[i]}°C</p>
                <p>Min: ${data.daily.temperature_2m_min[i]}°C</p>
                <p>Rain: ${data.daily.precipitation_probability_max[i]}%</p>
            `

            forecastDays.appendChild(card)
        }
            result.classList.remove("fade-in")
            void result.offsetWidth
            result.classList.add("fade-in")
            weatherIcon.textContent = icon
        })
        .catch((err) => {
            error.textContent = err.message
        })
        .finally(() => {
            btn.textContent = "Click"
            btn.disabled = false
        })
}

btn.addEventListener("click", function () {
    getWeather()
})

city.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        getWeather()
    }
})
