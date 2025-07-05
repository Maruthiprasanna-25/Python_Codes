tm=int(input("enter time minutes:"))
dm=int(input("enter distance in meters:"))
time=tm*60
dis=time*dm
fin_dis=dis//1000#instead of this we can also use math.floor(dis/1000)
print("Dstance covered:",fin_dis)