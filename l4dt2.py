from datetime import datetime, timedelta

today=datetime.now()
yesterday=datetime.now() - timedelta(days=1)
tomorrow=datetime.now() + timedelta(days=1)

print("today: ", today)
print("yesterday: ", yesterday)
print("tomorrow: ", tomorrow)