import time
import matplotlib.pyplot as plt
from termcolor import colored, cprint

def repeat():
    print("---------------------------------------------------")
    cprint("Do you want to calulate another Value (yes/no) : ","cyan",attrs=["blink"])
    flag=input()
    if(flag=="yes"):
        print("--------------------------------------------------")
        main()
    else:
        print("---------------------------------------------------")
        exit()

#main program starts here
print("---------------------------------------------------")   
cprint("Welcome to ECONOCODE","cyan",attrs=["blink"])
print("---------------------------------------------------")
time.sleep(1)
def main():
    inputValue=input(colored("Select One : ","red")+colored("[ PED | YED | XED | PES ]\n","yellow"))
    #check input value

    ##########XED##############
    if(inputValue=="ped"):
        #get inputs to check PED, Input can be have decimal point, So float
        i_p=float(input(colored("Initial Price of Anchor Milk Powder: ","green")))
        n_p=float(input(colored("New Price of Anchor Milk Powder: ","green")))
        i_q=float(input(colored("Initial Demand of Anchor Milk Powder: ","green")))
        n_q=float(input(colored("New Demand of Anchor Milk Powder: ","green")))
        #create plot 
        x = [i_q,n_q]
        y = [i_p,n_p]
        plt.plot(x, y,marker = '*')
        plt.xlabel("Demand")
        plt.ylabel("Price")
        plt.title("PED Graph")
        plt.show()
        #calculating the PED
        ped=((i_q-n_q)/(i_p-n_p))*(i_p/i_q)
        #printing the absoulute value of PED in 2 decimal points
        print(colored("PED value is : ","yellow")+colored("{:.2f}","green").format(abs(ped)))
        if(ped<1):
            print(colored("Inelastic Good","yellow"))
            print(colored("Increase in Total revenue","yellow"))if(i_p<n_p) else print(colored("Decrease in Total revenue","yellow"))
        elif(ped==1):
            print(colored("Unitary elastic Good","yellow"))
        elif(ped>1):
            print(colored("Elastic Good","yellow"))
            print(colored("Decrease in Total revenue","yellow"))if(i_p<n_p) else print(colored("Increase in Total revenue","yellow"))
        repeat()
    ##########XED##############
    elif(inputValue=="xed"):
        #Get Input Values
        i_d=float(input(colored("Good X : Initial Demand of Maliban Milk Powder: ","green")))
        n_d=float(input(colored("Good X : New Demand of Maliban Milk Powder: ","green")))
        i_p=float(input(colored("Good Y : Initial Price of Anchor Milk Powder: ","green")))
        n_p=float(input(colored("Good Y : New Price of Anchor Milk Powder: ","green")))
        #calculating the XED value
        xed=((i_d-n_d)/(i_p-n_p))*(i_p/i_d)
        print(colored("XED value is : ","yellow")+colored("{:.2f}","green").format(abs(xed)))
        repeat()

    ##########YED##############
    elif(inputValue=="yed"):
        #Get Input Values
        iIncome=float(input(colored("Initial Income of Customer : ","green")))
        nIncome=float(input(colored("New Income of Customer : ","green")))
        i_q=float(input(colored("Initial Demand of Anchor Milk Powder: ","green")))
        n_q=float(input(colored("New Demand of Anchor Milk Powder: ","green")))
        #calculating the YED value
        yed=((i_q-n_q)/(iIncome-nIncome))*(iIncome/i_q)
        print(colored("YED value is : ","yellow")+colored("{:.2f}","green").format(abs(yed)))
        repeat()

    ##########PES##############        
    elif(inputValue=="pes"):
        #Get Input Values
        i_p=float(input(colored("Initial Price of Anchor Milk Powder : ","green")))
        n_p=float(input(colored("New Price of Anchor Milk Powder : ","green")))
        i_q=float(input(colored("Supplied Initial Quantity of Anchor Milk Powder : ","green")))
        n_q=float(input(colored("Supplied New Quantity of Anchor Milk Powder : ","green")))
        #calculating the PES value
        pes=((i_q-n_q)/(i_p-n_p))*(i_p/i_q)
        print(colored("PES value is : ","yellow")+colored("{:.2f}","green").format(abs(pes)))
        repeat()
    ##########If user enters Invalid Data##############    
    else:
        print("Invalid Data")
        flag=input("Do you want to try again ? (yes/no)")
        if flag=="yes":
            main()
        else:
            time.sleep(2);
            exit()

main()