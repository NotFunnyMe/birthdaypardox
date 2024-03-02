import random
import datetime 

birthday = []
i = 0
while(i<50):
    year = random.randint(1907,2024)    #the oldeat person ever lived is 116 years old
    if year%4==0 and year%100!=0 or year%400==0:
        leap = 1
    else:
        leap = 0
    month = random.randint(1,12)
    if month == 2 and leap == 1:    #if month is feb and a leap year
        day = random.randint(1,29)
    elif month == 2 and leap == 0:  #if month is feb and not a leap year
        day = random.randint(1,28)  
    elif month == 7 and month == 8: #if month is july and august both have 31 days
        day = random.randint(1,31)
    elif month%2!=0 and month<7:    #if month are odd and less than 7  (January to June), they all have 31 days
        day = random.randint(1,31)
    elif month%2 == 0 and month>7 and month<12: #if month are even more than 7 (june, october etc.) and less than 12 they all have 31 days
        day = random.randint(1,31) 
    else:
        day = random.randint(1,30)

    dd = datetime.date(year,month,day)
    day_of_year = dd.timetuple().tm_yday    #get the day of the year
    i = i+1
    birthday.append(day_of_year)

birthday.sort()
i = 0
while(i<50):
    print(birthday[i])
    i = i+1