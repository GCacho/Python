from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("Ciudad de Mexico: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))

Caracas_timezone = pytz.timezone("America/Caracas")
Caracas_date = datetime.now(Caracas_timezone)
print("Caracas: ", Caracas_date.strftime("%d/%m/%Y, %H:%M:%S"))