import time
from datetime import datetime

seconds_since_epoch = time.time()
seconds_since_epoch_sn = time.time()
date_current = datetime.now()

seconds_since_epoch = "{:,.4f}".format(seconds_since_epoch)
seconds_since_epoch_sn = "{:.2e}".format(seconds_since_epoch_sn)
date_formatted = date_current.strftime("%b %d %Y")

print("Seconds since January 1, 1970:", seconds_since_epoch, "or", seconds_since_epoch_sn, "in scientific notation")
print(date_formatted)
