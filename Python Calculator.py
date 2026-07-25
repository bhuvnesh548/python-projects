#Python Calculator
choice=input("press s for start and x for exit : ")
while choice!="exit":
        if choice.lower()=="x":
                break
        else:
            number1=int(input("enter the first number: "))
            operation=input("enter a operation:(+,-,*,/,//,%)")
            number2=int(input("enter the second number: "))
            if operation=="+":
                    print(f"sum is {number1+number2}")
            elif operation=="-":
                    print(f"subtraction is {number1-number2}")
            elif operation=="*":
                    print(f"multipliction is {number1*number2}")
            elif operation=="/":
                    print(f"division is {number1/number2}")
            elif operation=="//":
                    print(f"floor division is {number1//number2}")
            elif operation=="%":
                    print(f"subtraction is {number1 % number2}")
            else:
                print("enter valid operator!!!")