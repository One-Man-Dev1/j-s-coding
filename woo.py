
import time

print("HELLO. welcome to the ice spice lemon sour lime juice ice website!")
print("we will give 8 free $25 packets if u do this!")
pro = input("do you wish to procees?: ")
if pro == "no":
    print("we dont need u. GET OUTTTTTTTTTTTTTT")
    time.sleep(5)
if pro == "yes":
    print("we need your ssn")
    
ssn1 = input("ssn here: ")
print("thank you for your ssn. now your credit card number")
ccn2 = input("ccn here: ")
print("now your routing number")
rrn = input("now your rn: ")

print("ssn:" + ssn1 + "-")
print("CCN:" + ccn2 + "-")
print("Rn:" + rrn + "-")




confirm = input("is this correct?: ")
if confirm == "no":
    print("aight. well do this program again")
    time.sleep(5)
if confirm == "yes":
    print(" u been haked")
    time.sleep(5)
