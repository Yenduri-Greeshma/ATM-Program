print("Welcome to ATM")
print("We hope you are Fine Today")
pin=18032004
n=int(input("Enter Password:"))
balance=70000
while n!=0:
        if n==pin:
           print("Correct Password")
           print("Do you Want to Credit or Debit")
           print("Choose(number) 1.credit 2.debit")
           c=int(input())
           if c==1 :
                 add=int(input("Enter the amount you want to credit:"))
                 Total=print("Total balance in Your account is",balance+add)
                 print("Thank you Visit again !\U0001F600")
                 break
           else:
                sub=int(input("Enter the amount you want to debit:"))
                if sub<balance:
                    print("Take your amount",sub)
                    print("Total amount in Your account is",balance-sub)
                    print("Thank you Visit again !\U0001F600")
                    break
                else:
                     print("Insufficient Balance")
        else:
            print("Incorrect password")
            n=int(input("Enter valid password:"))
