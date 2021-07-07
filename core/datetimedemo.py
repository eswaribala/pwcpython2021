import datetime

print(datetime.datetime.today())
print(datetime.datetime.today().strftime("%d/%m/%Y"))
print(datetime.datetime.today().strftime("%Y"))
doj=datetime.date(1991,6,2)
print("Date of Joining=%s" %(doj.strftime("%d/%m/%Y")))
exp=datetime.date.today()-doj
print("Experience=%d" %(int(exp.days/365)))
