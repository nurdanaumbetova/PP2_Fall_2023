from datetime import date, timedelta
dt = date.today()
print(f'current date: {dt}')
print(f'five days ago: {dt-timedelta(5)}')

