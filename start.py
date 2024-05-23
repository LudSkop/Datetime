from datetime import datetime

right_now = datetime.now()
print(f' ПОТОЧНИЙ РІК І ЧАС: {right_now}')
print(f'ПОТОЧНИЙ РІК: {right_now.year}')
print(f'ПОТОЧНИЙ МІСЯЦЬ: {right_now.month}')
print(f'ПОТОЧНИЙ ДЕНЬ: {right_now.day}')
print(f'ПОТОЧНИЙ  ЧАС: {right_now.hour}')
print(f'ПОТОЧНІ МИНУТИ: {right_now.minute}')
print(f'ПОТОЧНИЙ СЕКУНДИ: {right_now.second}')
print(f'ПОТОЧНИЙ МІКРОСЕКУНДИ: {right_now.microsecond}')
