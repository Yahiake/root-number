while True:
    i = float(input("\nEnter a number : "))
    k = float(input("\nEnter the degree of root : "))
    i = i**(1/k)
    print("\nYour ", k," degree root number is : ", i, "\n")
    check = str(input("Do you want to quit or start again? enter Y to restart or another key to end: "))
    if check == "y":
        continue
    elif check == "Y":
        continue
    else:
        print("\nGoodbye!")
        exit()
