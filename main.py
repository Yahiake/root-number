while True:
    i = float(input("\nEnter a number : "))
    k = int(input("\nEnter the degree of root : "))
    i = i**(1/k)
    k_str = str(k)
    if k_str.endswith("11"):
        print("\nYour", k, "\bth degree root number is : ", i,"\n")
    elif k_str.endswith("12"):
        print("\nYour", k, "\bth degree root number is : " ,i, "\n")
    elif k_str.endswith("13"):
        print("\nYour", k ,"\bth degree root number is : ", i, "\n")
    elif k_str.endswith("1"):
        print("\nYour", k, "\bst degree root number is : ", i,"\n")
    elif k_str.endswith("2"):
        print("\nYour", k, "\bnd degree root number is : " ,i, "\n")
    elif k_str.endswith("3"):
        print("\nYour", k ,"\brd degree root number is : ", i, "\n")
    else :
        print("\nYour", k ,"\bth degree root number is : " , i , "\n")
    check = str(input("Do you want to quit or start again? enter Y to restart or another key to end: "))
    if check == "y":
        continue
    elif check == "Y":
        continue
    else:
        print("\nGoodbye!")
        exit()
