import matplotlib.pyplot as graph
import time
def showInfo():
    print("Name : Raguraj S.")
    print("Index Number : 205080K")
    print()

def drawPlot(xvalue1,xvalue2,yvalue1,yvalue2,xlabel,ylabel,tableHeading):
    x = [xvalue1,xvalue2]
    y = [yvalue1,yvalue2]
    graph.plot(x, y)
    graph.xlabel(xlabel)
    graph.ylabel(ylabel)
    graph.title(tableHeading)
    graph.show()

def getRepetitionInputFromUser():
    print()
    print("What Elasticity Would you like to Measure ?")
    print("PED,YED,XED,PES\nSeperate By ',' eg: PED,YED,PES")
    print("__________________________________________________")
    calculate=input("Input : ")
    print("__________________________________________________")
    wantToCalculate=calculate.split(',')
    #get needed input for a problem from user
    initialPrice=float(input("Enter initial Price of Gas cylinder: "))
    newPrice=float(input("Enter new Price of Gas cylinder: "))
    initialDemand=float(input("Enter initial Demand of Gas cylinder: "))
    newDemand=float(input("Enter new Demand of Gas cylinder: "))
    initialDemandCooker=float(input("Enter initial Demand of Inductive Cooker: "))
    newDemandCooker=float(input("Enter new Demand of Inductive Cooker: "))
    initialIncome=newIncome=""
    if "YED" in wantToCalculate:
        initialIncome=float(input("Enter initial Income : "))
        newIncome=float(input("Enter new Income : "))
        print("__________________________________________________")
    for i in wantToCalculate:
        if i.lower()=="ped":
            ped(initialPrice,newPrice,initialDemand,newDemand)
        elif i.lower()=="xed":
            xed(initialDemandCooker,newDemandCooker,initialPrice,newPrice)
        elif i.lower()=="yed":
            yed(initialIncome,newIncome,initialDemand,newDemand)
        elif i.lower()=="pes":
            pes(initialPrice,newPrice,initialDemand,newDemand)
    inp=input("Would you like to view graph ? (y/n) : ")
    if inp.lower()=="y":
        if("PED" in wantToCalculate):
            drawPlot(initialDemand,newDemand,initialPrice,newPrice,"Demand","Price","GRAPH FOR PED")
        if("PED" in wantToCalculate):
            drawPlot(initialDemand,newDemand,initialPrice,newPrice,"Quantity Supplied","Price","GRAPH FOR PES")
        
    getFromUser=input("Would You like to calculate another problem ?(y/n) : ")
    if(getFromUser.lower()=="y"):
        getRepetitionInputFromUser()
    else:
        exit()
    

def ped(iPrice,nPrice,iQuantity,nQuantity):
    print("PED : PRICE ELASTICITY OF DEMAND")
    
    value=((iQuantity-nQuantity)/(iPrice-nPrice))*(iPrice/iQuantity)
    print("Change in Price of Gas cylinder is : ",abs(iPrice-nPrice))
    print("Change in Quantity Gas cylinder is : ",abs(iQuantity-nQuantity))
    print("PED is :{:.2f}".format(abs(value)))
    print("")
    time.sleep(1)

def xed(iDemand,nDemand,iPrice,nPrice):
    print("XED : CROSS ELASTICITY OF DEMAND")
    print("Change in Demand of Inductive Cooker is : ",abs(iDemand-nDemand))
    print("Change in Price of Gas Cylinder is : ",abs(iPrice-nPrice))
    value=((iDemand-nDemand)/(iPrice-nPrice))*(iPrice/iDemand)
    print("XED is :{:.2f}".format(abs(value)))
    print("")
    time.sleep(1)
    
def yed(iIncome,nIncome,iQuantity,nQuantity):
    print("YED : INCOME ELASTICITY OF DEMAND")
    print("Change in Income is of Customer : ",abs(iIncome-nIncome))
    print("Change in Quantity is of Gas cylinder : ",abs(iQuantity-nQuantity))
    value=((iQuantity-nQuantity)/(iIncome-nIncome))*(iIncome/iQuantity)
    print("YED is :{:.2f}".format(abs(value)))
    print("")
    time.sleep(1)

def pes(iPrice,nPrice,iQuantity,nQuantity):
    print("PES : PRICE ELASTICITY OF SUPPLY")
    print("Change in Price of Gas cylinder is : ",abs(iPrice-nPrice))
    print("Change in Quantity of Gas cylinder is : ",abs(iQuantity-nQuantity))
    value=((iQuantity-nQuantity)/(iPrice-nPrice))*(iPrice/iQuantity)
    print("PES is :{:.2f}".format(abs(value)))
    print("")
    time.sleep(1)

showInfo()
getRepetitionInputFromUser()
