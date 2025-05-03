#WEIGHTTT CONVERTERRRR
weight = float(input("enter you weight: "))
lbs_or_kg =input("enter lbs(L) or kg(K): ")
actualweight =lbs_or_kg.upper()
if actualweight=="K":
    weight=float(weight*2.2)
    print("your weight is: ",weight,"kg")
else:
    weight = float(weight / 2.2)
    print("your weight is: ", weight, "Lbs")

