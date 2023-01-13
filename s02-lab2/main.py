days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()

workdays.pop(6)
workdays.pop(5)

print("days: ", days)
print("workdays: ", workdays)