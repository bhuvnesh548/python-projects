#coffee machine 
menu={"espresso":{"ingredients":{"water":150,"coffee":25},"cost":10},
      "latte":{"ingredients":{"water":75,"milk":75,"coffee":25},"cost":15},
      "capucchino":{"ingredients":{"water":50,"milk":100,"coffee":25},"cost":20}
      }
sales=[]
profit=0
totalprofit=sum(sales)
resources={"water":1000,
           "milk":500,
           "coffee":200}
def resource_sufficient(ingredient):
    for item in ingredient:
        if ingredient[item]>resources[item]:
            print(f"sorry there is not enough {item}")
            return False
        else:
            resources[item]=resources[item]-ingredient[item]


print(f"{"welcome to the coffee machine":-^100}")
ison=True
while ison:
    choice=input("what do you want?(espresso/latte/capucchino) : ")
    if choice=="off":
        ison=False
    elif choice=="report":
        for i,j in resources.items():
            print(i,":",j,"ml")
        print("sales : ",sales)
        print("profit : ",profit,"₹")

    elif choice=="add":
        remained_water=resources["water"]
        remained_milk=resources["milk"]
        remained_coffee=resources["coffee"] 
        print(f"remaining water : {remained_water} ml")
        print(f"remaining milk : {remained_milk} ml") 
        print(f"remaining coffee : {remained_coffee} g")
        wate=int(input("fill water"))
        resources["water"]+=wate
        mil=int(input("fill milk"))
        resources["milk"]+=mil
        cof=int(input("fill coffee"))
        resources["coffee"]+=cof

    elif choice=="espresso":
        things=menu["espresso"]["ingredients"]
        # resource_sufficient(things)
        if resource_sufficient(things)!=False:       
            pay=int(input(f"please pay 10 ₹ :"))
            if pay==10: 
                print(f"here is your {choice}")
                sales.append(pay)
                profit=sum(sales)       
            
    elif choice=="capucchino":
        things=menu["capucchino"]["ingredients"]
        # resource_sufficient(things)  
        if resource_sufficient(things)!=False:     
            pay=int(input(f"please pay 20 ₹ :"))
            if pay==20: 
                print(f"here is your {choice}")
                sales.append(pay)
                profit=sum(sales)   
    elif choice=="latte":
        things=menu["latte"]["ingredients"]
        # resource_sufficient(things)
        if resource_sufficient(things)!=False:
            pay=int(input(f"please pay 15 ₹ :"))
            if pay==15: 
                print(f"here is your {choice}")
                sales.append(pay)
                profit=sum(sales)   
    else:
        print("enter a valid choice ")

