def convertTo24(time):
    time = time.strip().lower().replace(".", "")
    parts = time.split()
    hour, minute = map(int, parts[0].split(":"))
    amorpm = parts[1]

    if amorpm == "pm" and hour != 12:
        hour += 12
    elif amorpm == "am" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"

def timeDifference(current, meal):
    hour1, minute1 = map(int, current.split(":"))
    hour2, minute2 = map(int, meal.split(":"))

    total1 = hour1 * 60 + minute1
    total2 = hour2 * 60 + minute2

    diff = total2 - total1
    if diff < 0:
        diff += 24 * 60

    return diff

def timeToEat(time_str):
    time24 = convertTo24(time_str)

    mealTimes = ["07:00", "12:00", "19:00"]
    diffs = [timeDifference(time24, meal) for meal in mealTimes]

    minimum = min(diffs)
    hour = minimum // 60
    minutes = minimum % 60
    return [hour, minutes]

print(timeToEat("2:00 p.m."))
print(timeToEat("5:50 a.m."))
