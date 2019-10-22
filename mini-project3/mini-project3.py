# Напишите программу, которая в зависимости от кол-ва позиций(видов товаров), их цены и кол-ва подсчитает общую сумму
# покупки. В зависимости от вашего возраста и суммы покупки посчитает скидку(0.0015% за каждый год возраста).
# Программа должна проверять данные, которые поступают на вход. При сумме покупки более 10000 клиенту выдается
# карта постоянного клиента.
import local_mini_project_3 as lc
import random
print(lc.INP)
tr = 0
suma = 0
suma1 = 0
persent = 0
sale = 0
years1 = 0

print(lc.OLD)
years = int(input())
name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN',

              'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']        # An array containing the values of the months.

for month in name_month:
    print(month)
    print(lc.NUMBER)
    n = int(input())                                           # Input the amount of goods (typs)

    while n < 0:
        print(lc.NUMBER_0)
        n = int(input())

    while n != 0:
            n -= 1
            print(lc.PRICE)
            price = int(input())                               # Input price

            while price < 0:
                print(lc.PRICE_O)
                price = int(input())

            print(lc.NUMBER_01)                                # Input amount of goods
            number = int(input())

            while number < 0:
                print(lc.NUMBER_01_O)
                number = int(input())

            tr = number * price
            suma += tr

    print(lc.DOP)
    dop = str.lower(input())
    if dop == 'да':
            print(lc.PRICE)
            price = int(input())                               # Input price

            while price < 0:
                print(lc.PRICE_O)
                price = int(input())

            print(lc.NUMBER_01)                                # Input amount of goods
            number = int(input())

            while number < 0:
                print(lc.NUMBER_01_O)
                number = int(input())

            tr = number * price
            suma += tr


while years > 0:                                                # First discount calculation
    years1 += 0.0015
    years -= 1

print(lc.SUMA, suma)                                            # Output the amount
suma1 = suma

while suma1 > 0:                                                # Second discount calculation
    sale += 0.0035
    suma1 = suma1 // 10

persent = (sale + years1) * suma                                # Discount calculation

print(lc.SALE, "%.2f" % persent)                                # Output discount
print(lc.EXIT, "%.2f" % (suma - persent))                        # Output the amount to be paid

if suma > 10000:
    print(lc.CARD)                                              # Card
    m = (random.randint(0, 9999))
    print(m)
