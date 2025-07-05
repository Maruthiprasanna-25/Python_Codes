n=int(input("enter no of bottles:"))
crate=12
bo_fill=n//12
bo_left=n-(bo_fill*crate)
print("Full crates: ",bo_fill)
print("Leftover bottles: ",bo_left)