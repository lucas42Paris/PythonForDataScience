import time
from datetime import datetime

seconds_since_epoch = time.time()

seconds_standard = f"{seconds_since_epoch:,.4f}"
seconds_scientific = f"{seconds_since_epoch:.2e}"

current_date = datetime.now()

formatted_date = current_date.strftime("%b %d %Y")

print("Seconds since January 1, 1970:", seconds_standard, "or", seconds_scientific, "in scientific notation")
print(formatted_date)
