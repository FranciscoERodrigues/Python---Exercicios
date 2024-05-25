Dias = int(input('Dias: '))
Horas = int(input('Horas: '))
Minutos = int(input('Minutos: '))
Segundos = int(input('Segundos: '))

calculos = (Dias*86400) + (Horas*3600) + (Minutos*60) + Segundos

print(" A quantidade de segundos é", calculos)
