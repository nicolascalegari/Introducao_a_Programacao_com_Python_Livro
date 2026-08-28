dia = int(input("Informe a quantidade de dias: "))

hora = int(input("Informe a quantidade de horas: "))

minuto = int(input("Informe a quantidade de minutos: "))

segundo = int(input("Informe a quantidade de segundos: "))

total = segundo + (minuto * 60) + (hora * 3600) + (dia * 86400)

print(f"Total de {total} segundos")