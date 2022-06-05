import datetime

my_time = datetime.datetime.now()

my_day = datetime.date.today()

print(my_time)
print(my_day)
print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')

#Tabla de codigo de formato

#   %Y - Year
#   %m - Month
#   %d - Day
#   %H - Hour
#   %M - Minute
#   %S - Second


fecha = datetime.datetime.now()
print(fecha)

print("-------------------")

fecha1 = fecha.strftime("%d/%m/%Y")
print(f'Formato Latam: {fecha1}')

fecha1 = fecha.strftime("%m/%d/%Y")
print(f'Formato USA: {fecha1}')

fecha1 = fecha.strftime("Estamos en el año %Y")
print(f'Formato Random: {fecha1}')

