### Dates ###

# Son objetos
# De la librería datetime importame la clase datetime
from datetime import datetime
# nombre del objeto = nombre de las función importada "datetime"

def print_date(date):
    print("Año:",date.year)
    print("Mes:",date.month)
    print("Día:",date.day)
    print("Hora:",date.hour)
    print("Minutos:",date.minute)
    print("Segundos:",date.second)
    print(date.timestamp())


now = datetime.now()

print_date(now)

# Captura el momento exacto a partir de la fecha inicio que recoge el lenguaje ( 1970 )
# En todos los lugares del mundo resulta el mismo número
timestamp = now.timestamp()


# Crear un objeto con una fechar predefinida
# {Año, mes ,día}[hora,minutos,segundos]
year_2024 = datetime(2024, 1, 1)

print_date(year_2024)

# De la librería datetime importa la clase time
# Es similar a datetime pero esta no tiene fecha, trabaja con horas min seg ..
from datetime import time

# nombre = clase(horas,minutos,segundos) ó vaío 
current_time = time()

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Trabaja con fechas ( date ) de la librería datetime
from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

# Inicializado introduciendo parámetros a mano
current_date = date(2021, 2, 12)

print(current_date) 

# Calcular los días que quedan hasta 2024 ( solo se pueden calcular objetos del mismo tipo )
diff = year_2024 - now

print(diff)


# Trbaja con franjas de fechas con valores absolutos
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)


