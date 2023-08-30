import time
import datetime

timestamp = time.time()

current_date = datetime.datetime.now()
day = current_date.day
month = current_date.strftime("%b")
year = current_date.year

timestamp_formatted = "{:,.4f}".format(timestamp)
timestamp_scientific = "{:.2e}".format(timestamp)

print("Seconds since January 1, 1970:", timestamp_formatted, "or", timestamp_scientific, "in scientific notation")
print(month, day, year)
