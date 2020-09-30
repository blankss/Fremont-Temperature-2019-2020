import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/2212342.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        high = row[7]
        low = row[8]
        if high == '' or low == '':
            continue
        else:
            high = int(row[7])
            low = int(row[8])
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title('Daily high and low temperatures in Fremont 2019-2020', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()