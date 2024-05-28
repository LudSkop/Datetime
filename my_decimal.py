# Налаштування точності.
from decimal import Decimal, getcontext

numbers = 0.2 + 0.1 + 0.3 - 0.5
print(numbers)
result = Decimal('0.2') + Decimal('0.1') + Decimal('0.3') - Decimal('0.5')
print(result)

n = Decimal('10') / Decimal('3')
print(n)
print(type(n))
# В методі getcontext є атрибут .prec  він керує точністю обчислення.
getcontext().prec = 6
n = Decimal('10') / Decimal('3')  # 3.33333
print(n)
n = Decimal('1') / Decimal('3')
print(n)                         # 0.333333
