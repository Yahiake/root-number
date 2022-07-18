while True:
    i = float(input("\nEnter a number : "))
    k = int(input("\nEnter the degree of root : "))
    i = i**(1/k)
    if k%10 == 1:
        print("\nYour", k, "st degree root number is : ", i,"\n")
    elif k%10 == 2:
        print("\nYour", k, "nd degree root number is : " ,i, "\n")
    elif k%10 == 3:
        print("\nYour", k ,"rd degree root number is : ", i, "\n")
    else :
        print("\nYour", k ,"th degree root number is : " , i , "\n") #ordinal numbers are not perfect, works well until 20 after that it prints th which is wrong in some cases
    check = str(input("Do you want to quit or start again? enter Y to restart or another key to end: "))
    if check == "y":
        continue
    elif check == "Y":
        continue
    else:
        print("\nGoodbye!")
        exit()
