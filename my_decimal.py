# Налаштування точності.
#from decimal import Decimal, getcontext
from decimal import Decimal
numbers = 0.2 + 0.1 + 0.3 - 0.5
print(numbers)
result = Decimal('0.2') + Decimal('0.1') + Decimal('0.3') - Decimal('0.5')
print(result)

n = Decimal('10') / Decimal('3')
print(n)
print(type(n))
# В методі getcontext є атрибут .prec  він керує точністю обчислення.
#getcontext().prec = 6
n = Decimal('10') / Decimal('3')  # 3.33333
print(n)
n = Decimal('1') / Decimal('3')
print(n)                          # 0.333333

# Створення Decimal із дійсних чисел.Перед тим як додавати float потрібно перевести до str.

print(0.1 + 0.2)                                #0.30000000000000004

print(Decimal(0.1) + Decimal(0.2))              #0.3000000000000000166533453694
print(Decimal(str(0.1)) + Decimal(str(0.2)))    # 0.3

