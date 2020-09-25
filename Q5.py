# Input employee information from the user including his employee id, name, address, salary,
# birth date and date of joining. Find the age of person when he joined company (in years) and his
# experience till date (in months). Also print the date when his probation period is over, assuming that
# probation period is of 90 days from date of joining.

from datetime import *

eid = int(input("Enter Employee Id"))
ename = input("Enter Employee Name")
eadd = input("Enter Employee Address")
esalary = int(input("Enter Employee Salary"))
edob = input("Enter Date Of Birth in DD/MM/YYYY")
edobData = edob.split("/")
edobDay = int(edobData[0])
edobMonth = int(edobData[1])

edobYear = int(edobData[2])
edoj = input("Enter Date Of Joining in DD/MM/YYYY")
edojData = edoj.split("/")
edojDay = int(edojData[0])
edojMonth = int(edojData[1])
edojYear = int(edojData[2])

# To find Age of Employee at the Time of Joining
today = date.today()
currentMonth = datetime.now().month
eage = (edojYear - edobYear)
print("Age of Employee at the time of Joining is", eage)

# To find Experience of Employee till date in months
currentYear = datetime.now().year
expYear = (currentYear - edojYear)
expMonth = (currentMonth - edojMonth)
totalexp = expYear * 12 + expMonth
print("Total Experience Of Employee(in months) is", totalexp)

# To find probation period
currentDay = datetime.now().day
edojDate = datetime.strptime(edoj, "%d/%m/%Y")

probDate = edojDate + timedelta(90)
print("Probation period ends/ended on", probDate.strftime("%d/%m/%Y"))

