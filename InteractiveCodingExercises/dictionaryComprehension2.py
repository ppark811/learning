weather_c = {"Mon": 12, "Tues": 14, "Wed": 15, "Thur": 14, "Fri": 21, "Sat": 22,"Sun": 24}

weather_f = {day: (temp_c* 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
 