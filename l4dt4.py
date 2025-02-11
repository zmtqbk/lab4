from datetime import datetime

fdate=input("input in format: YYYY-MM-DD HH:MM:SS ")
sdate=input("input in format: YYYY-MM-DD HH:MM:SS ")

date1=datetime.strptime(fdate, "%Y-%m-%d %H:%M:%S")
date2=datetime.strptime(sdate, "%Y-%m-%d %H:%M:%S")

diff=date2-date1
diffsec=diff.total_seconds()

print("diff in sec: ", diffsec)