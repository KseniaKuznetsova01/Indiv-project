#Алиса решила открыть свою кофейню. Ей нужно снять в аренду помещение площадью 30м^2(зал для клиентов занимает 3/5 от всей площади) по цене T за 3 м^2,
# купить столы и стулья(на 3м^2 требуется один комплект, который состоит из одного стола и 6 стульев) по цене S за один стол(один стул стоит в 3 раза меньше),
# 2 кофемашины по цене в три раза дороже чем один комплект мебели, состоящий из стола и стульев, набор посуды по цене равной 140% от стоимости комплекта мебели.
# Также ей придется оплатить коммунальные услуги (вода, электричество, отопление), цена которых  за один месяц составляет 80% от стоимости двух кофемашин.
# На продукты в первый месяц Алиса должна потратить 55% от средней стоимости комплектов мебели, двух кофемашин и посуды.
# Каждый месяц затраты на продукты будут увеличиваться на N тыс. руб.
# За каждый месяц работы с Алисы будет взят фиксированный налог, который составит 3% с дохода в первый месяц работы.
# Доход в месяц составит 175% от суммы затрат на продукты за месяц.. У Алисы есть 500 000 руб.
# На какую сумму она должна взять кредит в банке,
# чтобы ей хватило денег на закупку мебели, кофемашин, посуды, оплаты коммунальных услуг и закупку продуктов,
# если она рассчитывает бюджет на N месяцев. При условии, что каждый месяц банк будет забирать 10% с первоначального дохода кофейни.
# (Т, S, N – целые числа, вводятся с клавиатуры через пробел).
T, S, N = map(int, input().split()) #Price for sale, price for table, month
Area = 30 #Room size
Tables = (Area*3/5)//3 #Quantity of tables
Chairs = Tables * 6 #Number of chairs
TabCha = S + S//3*6 #One table + 6 chairs
SummF = ((S * Tables) + (S/3 * Chairs )) # Price for all furniture
SummC = TabCha*2 #Price for coffee machines
SummD = TabCha/100*140 #Price for tableware
Utilities = SummC / 100 * 80 #Price for utilities for all time
Products = ((SummF + SummC + SummD)/3 /100*55)*N + ((N-1)*1000) #Price for all products
TR = Products /100 * 175 #Income
Tax = TR/100*3 * N
BankTax = TR/100*10 *N
All_need_Summ = SummF + SummC + SummD + Utilities + Products + TR + Tax + BankTax - 500000
print('Один комплект мебели стоит:', round(TabCha), 'рублей', '\nВся мебель для зала будет стоить:', round(SummF),'рублей', '\nКофемашины будут стоить:', round(SummC),'рублей', '\nПосуда будет стоить:', round(SummD),'рублей', '\nЗа коммунальные услуги за заданный период Алиса заплатит:', round(Utilities),'рублей', '\nЗакупка продуктов на заданный период будет стоить: ', round(Products),'рублей', '\nДоход за заданный период составит:', round(TR),'рублей', '\nНалог будет составлять:', round(Tax),'рублей', '\nБанку нужно будет выплатить:', round(BankTax), 'рублей')
if (All_need_Summ > 0):
    print('Алисе потребуется взять кредит на сумму:', round(All_need_Summ), 'рублей.')
else:
    print('Алисе хватит денег, которые у нее есть')