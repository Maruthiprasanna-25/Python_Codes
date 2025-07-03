v=int(input("enter total no of vehicles:"))
w=int(input("enter total no of wheels:"))
if w<2 or w%2!=0 or v>w:
    print("invalid")
else:
    fw=(w-2*v)//2
    tw=v-fw
    if fw<0 or tw<0:
        print("invalid input")
    else:
        print(tw,fw)
    