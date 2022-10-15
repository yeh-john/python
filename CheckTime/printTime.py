from datetime import datetime
import pytz

# Setting time
timezone_tw = pytz.timezone('Asia/Taipei')
time_tw = datetime.now(timezone_tw)
print("Next upload time is: ", time_tw.strftime('%H:%M:%S'))
