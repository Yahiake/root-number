while True:
    i = float(input("Enter a number : "))
    k = int(input("Enter the degree of root : "))
    i = i**(1/k)
    print(f"Your degree {k} root number is: {i}")
    check = str(input("Do you want to quit or start again? enter Y to restart or another key to end: "))
    if check in ["y", "Y"]:
        continue
    else:
        print("Goodbye!")
        exit()
