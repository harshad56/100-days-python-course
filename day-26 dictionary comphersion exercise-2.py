weather_c = {
    "monday": 12,
    "tuesdasy": 14,
    "wednesday": 15,
    "thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "sunady": 24
}

# to convert the  weather_c to weather_f
weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)
