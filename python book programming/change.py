def main():
    print ("Change Counter")
    print ("Please entere the count of each coin type. ")
    quarters = float(input("Qurateres :  "))
    dimes = float( input ("Dimes: "))
    nickels = float (input ("Nickels: "))
    pennies = float(input ("Pennies : "))
    total = float()
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print ("The total value of ypur charge is : ", total)

main()
