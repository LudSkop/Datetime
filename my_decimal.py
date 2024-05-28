# Налаштування точності.
from decimal import Decimal, getcontext

numbers = 0.2 + 0.1 + 0.3 - 0.5
print(numbers)
result = Decimal('0.2') + Decimal('0.1') + Decimal('0.3') - Decimal('0.5')
print(result)

n = Decimal('1') / Decimal('3')
print(n)