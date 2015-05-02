def forecast(days):
    result = {}
    max_weather = ""
    current_max = 0
    for day in days:
        if day not in result:
            result[day] = 0
        result[day] = result[day] + 1
    for weather in result:
        if result[weather] > current_max:
            max_weather = weather
            current_max = result[weather]
        
    return result, max_weather, current_max
days = ["snow", 'rain', "snow", "rain", 
'rain', 'rain', "sunshine"]
print(forecast(days))


def forecast2(days):
    return {weather: days.count(weather) for weather in days}

print(forecast2(days))
