from datetime import datetime, timedelta

cd=datetime.now()
mcr=cd.replace(microsecond=0)
print("curdate without microsec: ", mcr)