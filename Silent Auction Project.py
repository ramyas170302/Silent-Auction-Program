import os
dict={}
highest=0
winner=" "
def program():
    print("WELCOME TO THE SILENT AUCTION PROGRAM")
    name = input("What is your name?:\n ")
    amt=int(input("How many biddings do you have?:\n "))
    dict[name]=amt
program()
flag=True
while flag:
    next=input("Do you have other biddings? (y/n):\n ").lower()
    if next=="y":
        os.system("cls")
        program()
    else:
        for name in dict:
            if dict[name]>highest:
                highest=dict[name]
                winner=name
        print(f"highest bidding amount:{highest} from {winner}")
        flag=False

