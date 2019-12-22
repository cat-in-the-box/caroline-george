#Tip Calculator for 20% tips
bill = input("What was your bill? ")
tippercent = .2
tipamount = tippercent*float(bill)
total = float(tipamount) + float(bill)
print("Your 20% tip should be $", tipamount, ". Your total comes to $", total, ". ")

#Tip Calculator for custom tips
bill = input("What was your bill? ")
customtip = input("What percentage would you like to leave as a tip? ")
customtipamount = float(customtip)/100*float(bill)
customtotal = float(customtipamount) + float(bill)
print("Your", str(customtip)+"% tip should be $", customtipamount, ". Your total comes to $", customtotal, ". ")

#Suggested Tip Calculator
satisfaction = input("How was your dining experience today?\nA) Bad\nB) Average\nC) Amazing \n")
if satisfaction == "A":
    print("I'm sorry to hear that. I suggest you only leave a 15% tip.")
    picktip = input("Would you like to\nA)Leave a 15% tip\nB)Leave a custom tip\n")
    if picktip == "A":
        bill = input("What was your bill? ")
        tippercent = .15
        tipamount = tippercent*float(bill)
        total = float(tipamount) + float(bill)
        print("Your 15% tip should be $", tipamount, ". Your total comes to $", total, ". ")
    if picktip == "B":
        bill = input("What was your bill? ")
        customtip = input("What percentage would you like to leave as a tip? ")
        customtipamount = float(customtip)/100*float(bill)
        total = float(customtipamount) + float(bill)
        print("Your", str(customtip)+"% tip should be $", customtipamount, ". Your total comes to $", total, ". ")
if satisfaction == "B":
    print("That's decent. I suggest you leave a 20% tip.")
    picktip = input("Would you like to\nA)Leave a 20% tip\nB)Leave a custom tip\n")
    if picktip == "A":
        bill = input("What was your bill? ")
        tippercent = .20
        tipamount = tippercent*float(bill)
        total = float(tipamount) + float(bill)
        print("Your 20% tip should be $", tipamount, ". Your total comes to $", total, ". ")
    if picktip == "B":
        bill = input("What was your bill? ")
        customtip = input("What percentage would you like to leave as a tip? ")
        customtipamount = float(customtip)/100*float(bill)
        total = float(customtipamount) + float(bill)
        print("Your", str(customtip)+"% tip should be $", customtipamount, ". Your total comes to $", total, ". ")
if satisfaction == "C":
    print("That's awesome!! I suggest you leave a 25% tip.")
    picktip = input("Would you like to\nA)Leave a 25% tip\nB)Leave a custom tip\n")
    if picktip == "A":
        bill = input("What was your bill? ")
        tippercent = .25
        tipamount = tippercent*float(bill)
        total = float(tipamount) + float(bill)
        print("Your 25% tip should be $", tipamount, ". Your total comes to $", total, ". ")
    if picktip == "B":
        bill = input("What was your bill? ")
        customtip = input("What percentage would you like to leave as a tip? ")
        customtipamount = float(customtip)/100*float(bill)
        total = float(customtipamount) + float(bill)
        print("Your", str(customtip)+"% tip should be $", customtipamount, ". Your total comes to $", total, ". ")