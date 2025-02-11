from datetime import datetime, timedelta 

cd=datetime.now()
nd=cd - timedelta(days=5)
print("current data: ", cd)
print("new data: ", nd)