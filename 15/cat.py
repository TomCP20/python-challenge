
"""cat"""
import datetime

years = [year for year in range(1016, 1997, 20) if datetime.date(year, 1, 26).isoweekday() == 1]
print(datetime.date(years[-2], 1, 27))
# 1756-01-27 mozart birthday
