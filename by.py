import time
import decimal

print('-=' * 20)
print(' ' * 15, 'TROCO')
print('-=' * 20)

quanto_custou = decimal.Decimal(input('\033[1:32mTotal da venda: R$'))
recebeu = decimal.Decimal(input('\033[1:34mQuanto recebeu: R$'))
cedula = 200
total = recebeu - quanto_custou
print(f'\033[mO troco é de R${total:.2f}')
contador = 0

while True:
    if total >= cedula:
        total = total - cedula
        contador = contador + 1

else:
    if contador > 0:
     print(f'\nTotal de {contador} de R${cedula:.2f}', end='')

if cedula == 200:
    cedula = 100
    contador = 0

elif cedula == 100:
    cedula = 50
    contador = 0

elif cedula == 50:
    cedula = 20
    contador = 0

elif cedula == 20:
    cedula = 10
    contador = 0

elif cedula == 10:
    cedula = 5
    contador = 0

elif cedula == 5:
    cedula = 2
    contador = 0

elif cedula == 2:
    cedula = 1
    contador = 0

elif cedula == 1:
    cedula = decimal.Decimal(0.50)
    contador = 0

elif cedula == decimal.Decimal(0.50):
    cedula = decimal.Decimal(0.25)
    contador = 0

elif cedula == decimal.Decimal(0.25):
    cedula = decimal.Decimal(0.10)
    contador = 0

elif cedula == decimal.Decimal(0.10):
    cedula = decimal.Decimal(0.05)
    contador = 0

elif total > 0 and total <= 0.05:
    contador = 1
    print(f'\nTotal de {contador} de R${cedula:.2f}', end='')

    #break

elif total <= 0.05:
    #break
    time.sleep(0.5)