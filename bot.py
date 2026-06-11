import requests

try:
    weather_response = requests.get(
        "https://wttr.in/?format=3"
    )

    weather = weather_response.text

except Exception:
    weather = "Weather unavailable"

try:
    quote_response = requests.get(
        "https://zenquotes.io/api/random"
    )

    quote_data = quote_response.json()

    quote = quote_data[0]["q"]
    author = quote_data[0]["a"]

except Exception:
    quote = "Stay positive."
    author = "Pulse"

summary = f"""
Daily Pulse

Weather:
{weather}

Quote:
"{quote}"

- {author}
"""

print(summary)

with open(
    "daily_summary.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(summary)