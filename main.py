# main.py

from finance_utils import round_to_nearest

value = 123.45
nearest = 0.05

try:
    rounded_value = round_to_nearest(value, nearest)
    print(f'Округленное значение {value} до ближайших {nearest} равно {rounded_value}')
except ValueError as e:
    print(e)