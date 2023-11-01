year = int(input("which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leeap yar")
        else:
            print("not leap year")
    else:
        print("leap year.")
else:
    print("not a leep year")
