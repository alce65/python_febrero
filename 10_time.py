import datetime

now = datetime.datetime.now()
print(now)

print(now.day)
print(now.month)
print(now.year)

fecha = datetime.datetime(2000, 1, 1)

print(fecha)

print(now - fecha)

print(fecha.strftime('%c'))
print(fecha.strftime('%x'))