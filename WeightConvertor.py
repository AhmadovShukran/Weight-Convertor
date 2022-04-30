

while True:
    choice=input("Kg to Lbs ---> 1 or Lbs to Kg ---> 2 ")
    if int(choice)==1:
        kg=int(input("Please input mass: "))
        print("Approximate lb is {}".format(kg*(2.205)))
        choice = input("Will you continue or not (yes/no): ")
        if choice == "no":
            break
    elif int(choice)==2:
        lbs=int(input("Please input mass: "))
        print("Approximate kg is {}".format(lbs//(2.205)))
        choice = input("Will you continue or not (yes/no): ")
        if choice == "no":
            break
    else:
        print("Please make right choice.")