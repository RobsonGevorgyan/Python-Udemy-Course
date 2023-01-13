price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus
print(price)

price = 123

price = price - bonus if bonus_granted == True else 0
print(price)

###################################

rating = 6

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

result = "very good" if rating == 5 else print("good") if rating == 4 else print("week")
print(result)

###################################

today_weekday = "czwartek"

if today_weekday =="poniedzialek":
    print("ja nie mogę Bo pomagam mamie")
elif today_weekday =="wtorek" or today_weekday =="sroda":
    print("Ty masz w domu pranie")
elif today_weekday == "czwartek":
    print("dwa zebrania")
elif today_weekday == "sobota":
    print("nie możesz Bo na lekcje ganiasz")
else:
    print("niedziela bedzie dla nas")

result2 = "ja nie mogę Bo pomagam mamie" if today_weekday =="poniedzialek" else "Ty masz w domu pranie" if today_weekday =="wtorek" or today_weekday =="sroda" else "dwa zebrania" if today_weekday == "czwartek" else "nie możesz Bo na lekcje ganiasz" if today_weekday == "sobota" else "niedziela bedzie dla nas"
print(result2)