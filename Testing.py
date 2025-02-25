from datetime import datetime

print(str(datetime.now())[str(datetime.now()).index(' '):str(datetime.now()).index(' ') + 9])
print(datetime.now())