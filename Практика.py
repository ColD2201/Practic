import datetime
day = int(input("День: "))
mouth = int(input("Месяц: "))
year = int(input("Год: "))
x = datetime.datetime(year,mouth,day)
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Год високосный.')
else:
    print('Год не високосный.')
print(x.strftime("%a"))
real_date = datetime.datetime.now().year
print("Ваш возраст:", str(real_date - year))
print("Ваша полная дата рождения: ",str(day),".",str(mouth),".",str(year), sep="")
