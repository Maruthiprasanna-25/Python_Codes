year=int(input("enter year:"))
day=input("enter day:").strip().split()
is_leap=(year%4==0 and (year%100!=0 or year%400==0))
is_day=day in ["saturday","sunday"]
if is_leap:
    if is_day:
        print(year,"is a leap year with weak end")
    else:
        print(year,"is a leap year with weak days")
else:
    print(year,"is not a leap year")