i=0

while i<=1:

    import math as m 
    import time as t 



    print('1.length')
    print('2.weight')
    print('3.temperature')

    t.sleep(1)

    qtc = int(input("name which quantity to convert "))        # qtc is quantity variable

    if qtc == 1:
        
        print("1.centimeter")
        print("2.inch")
        print('3.foot')
        print('4.meter')
        print('5.kilometers')

        t.sleep(1)

        tco = int(input('name the measurement you have '))    #tco is to convert variable

        print("1.centimeter")
        print("2.inch")
        print('3.foot')
        print('4.meter')
        print('5.kilometers')

        tbc = int(input('measure to convert to '))            #tbc is to be converted variable


        if tco == 1 and tbc == 1:
            print('enter a valid statement')

        if tco == 1 and tbc == 2:
            val1 = float(input("enter value in centimeter "))

            ans1 = val1/2.54

            if ans1 >= 1:
                print(ans1,'inch')
            
            else:
                print(ans1,'inches')


        if tco == 1 and tbc == 3:
            val1 = float(input('enter value in centimeter'))

            ans1 = val1/30.48

            if ans1 >= 1:
                print(ans1,'feet')
            
            else:
                print(ans1,'foot')

        
        if tco == 1 and tbc == 4:
            val1 = float(input('enter value in centimeter'))

            ans1 = val1/100

            if ans1 >= 1:
                print(ans1,'meter')
            
            else:
                print(ans1,'meters')

        
        if tco == 1 and tbc == 5:
            val1 = float(input('enter value in centimeter'))

            ans1 = val1/100000

            if ans1 >= 1:
                print(ans1,'kilometer')
            
            else:
                print(ans1,'kilometers')

        if tco == 2 and tbc == 1:
            val1 = float(input('enter value in inches '))

            ans1 = val1*2.54

            if ans1 >= 1:
                print(ans1,'centimeter')
            
            else:
                print(ans1,'centimeters')

        
        elif tco == 2 and tbc == 2:
            print('enter a valid statement')

        elif tco == 2 and tbc == 3:
            val1 = float(input('enter value in inches '))

            ans1 = val1/12

            if ans1 >= 1:
                print(ans1,'feet')
            
            else:
                print(ans1,'foot')

        elif tco == 2 and tbc == 4:
            val1 = float(input('enter value in inches '))

            ans1 = val1/39.37

            if ans1 >= 1:
                print(ans1,'meter')
            
            else:
                print(ans1,'meters')

        elif tco == 2 and tbc == 5:
            val1 = float(input('enter value in inches '))

            ans1 = val1/39370

            if ans1 >= 1:
                print(ans1,'kilometer')
            
            else:
                print(ans1,'kilometers')

        elif tco == 3 and tbc == 1:
            val1 = float(input('enter value in foot '))

            ans1 = val1*3.48

            if ans1 >= 1:
                print(ans1,'centimeter')
            
            else:
                print(ans1,'centimeters')

        
        elif tco == 3 and tbc == 2:
            val1 = float(input('enter value in foot '))

            ans1 = val1*12

            if ans1 >= 1:
                print(ans1,'inch')
            
            else:
                print(ans1,'inchess')

        elif tco == 3 and tbc == 3:
            print('enter a valid statement ')

        elif tco == 3 and tbc == 4:
            val1 = float(input('enter value in foot '))

            ans1 = val1/3.281

            if ans1 >= 1:
                print(ans1,'meter')
            
            else:
                print(ans1,'meters')

        elif tco == 3 and tbc == 5:
            val1 = float(input('enter value in foot '))

            ans1 = val1/3281

            if ans1 >= 1:
                print(ans1,'kilometer')
            
            else:
                print(ans1,'kilometers')

        elif tco == 4 and tbc == 1:
            val1 = float(input('enter value in meters '))

            ans1 = val1*100

            if ans1 >= 1:
                print(ans1,'centimeter')
            
            else:
                print(ans1,'centimeters')
            
        elif tco == 4 and tbc == 2:
            val1 = float(input('enter value in meters '))

            ans1 = val1*39.37

            if ans1 >= 1:
                print(ans1,'inch')
            
            else:
                print(ans1,'inches')

        elif tco == 4 and tbc == 3:
            val1 = float(input('enter value in meters '))

            ans1 = val1*3.281

            if ans1 >= 1:
                print(ans1,'feet')
            
            else:
                print(ans1,'foot')

        elif tco == 4 and tbc == 4:
            print('enter a valid statement ')

        elif tco == 4 and tbc == 5:
            val1 = float(input('enter value in meters '))

            ans1 = val1/1000

            if ans1 >= 1:
                print(ans1,'kilometer')

            else:
                print(ans1,'kilometers') 
        
        elif tco == 5 and tbc == 1:
            val1 = float(input('enter value in kilometers '))

            ans1 = val1*100000

            if ans1 >= 1:
                print(ans1,'centimeter')

            else:
                print(ans1,'centimeters') 

        
        elif tco == 5 and tbc == 2:
            val1 = float(input('enter value in kilometers '))

            ans1 = val1*39370

            if ans1 >= 1:
                print(ans1,'inch')

            else:
                print(ans1,'inches')

        elif tco == 5 and tbc == 3:
            val1 = float(input('enter value in kilometers '))

            ans1 = val1*3281

            if ans1 >= 1:
                print(ans1,'feet')

            else:
                print(ans1,'foot')

        elif tco == 5 and tbc == 4:
            val1 = float(input('enter value in kilometers '))

            ans1 = val1*1000

            if ans1 >= 1:
                print(ans1,'meter')

            else:
                print(ans1,'meters')

        elif tco == 5 and tbc == 5:
            print("enter a valid statement")


    elif qtc == 2:
        print("1.grams")
        print("2.kilograms")
        print("3.pounds")
        print('4.ounces')

        t.sleep(1)

        tco = int(input('name the measurement you have '))

        print("1.grams")
        print("2.kilograms")
        print("3.pounds")
        print('4.ounces')

        t.sleep(1)

        tbc = int(input('name the measurement to convert into '))

        if tco == 1 and tbc == 1:
            print("enter a valid statement")

        elif tco == 1 and tbc == 2:
            
            val1 = float(input("enter the value in grams "))

            ans1 = val1/1000

            if ans1 >= 1:
                print(ans1,'kilogram')

            else:
                print(ans1,'kilograms')


        elif tco == 1 and tbc == 3:
            val1 = float(input("enter the value in grams "))

            ans1 = val1/454

            if ans1 >= 1:
                print(ans1,'pound')

            else:
                print(ans1,'pounds')

            
        elif tco == 1 and tbc == 4:
            val1 = float(input("enter the value in grams "))

            ans1 = val1/28.35

            if ans1 >= 1:
                print(ans1,'ounce')

            else:
                print(ans1,'ounces')

        elif tco == 2 and tbc == 1:
            val1 = float(input("enter the value in kilograms "))

            ans1 = val1*1000

            if ans1 >= 1:
                print(ans1,'gram')

            else:
                print(ans1,'grams')

        elif tco == 2 and tbc == 2:
            print("enter a valid statement")

        elif tco == 2 and tbc == 3:
            val1 = float(input("enter the value in kilograms "))

            ans1 = val1*2.205

            if ans1 >= 1:
                print(ans1,'pound')

            else:
                print(ans1,'pounds')

        elif tco == 2 and tbc == 4:
            val1 = float(input("enter the value in kilograms "))

            ans1 = val1*35.274

            if ans1 >= 1:
                print(ans1,'ounce')

            else:
                print(ans1,'ounces')

        elif tco == 3 and  tbc == 1:
            val1 = float(input("enter the value in pounds "))

            ans1 = val1*454

            if ans1 >= 1:
                print(ans1,'gram')

            else:
                print(ans1,'grams')

        elif tco == 3 and tbc == 2:
            val1 = float(input("enter the value in pounds "))

            ans1 = val1/2.205

            if ans1 >= 1:
                print(ans1,'kilogram')

            else:
                print(ans1,'kilograms')

        elif tco == 3 and tbc == 3:
            print("enter a valid statement")

        elif tco == 3 and tbc == 4:
            val1 = float(input("enter the value in pounds "))

            ans1 = val1*16

            if ans1 >= 1:
                print(ans1,'ounce')

            else:
                print(ans1,'ounces')

        elif tco == 4 and tbc == 1:
            val1 = float(input("enter the value in ounces "))

            ans1 = val1*28.35

            if ans1 >= 1:
                print(ans1,'gram')

            else:
                print(ans1,'grams')

        elif tco == 4 and tbc == 2:
            val1 = float(input("enter the value in ounces "))

            ans1 = val1/35.274

            if ans1 >= 1:
                print(ans1,'kilogram')

            else:
                print(ans1,'kilograms')

        elif tco == 4 and tbc == 3:
            val1 = float(input("enter the value in ounces "))

            ans1 = val1/16

            if ans1 >= 1:
                print(ans1,'pound')

            else:
                print(ans1,'pounds')

        elif tco == 4 and tbc == 4:
            print("enter a valid statement")

    elif qtc == 3:
        print('1.degree celsius')
        print('2.degree fahrenheit')

        tbc = int(input("enter which measurement you have "))

        print('1.degree celsius')
        print('2.degree fahrenheit')

        tco = int(input("enter which statement to convert to "))


        if tbc == 1 and tco == 1:
            print("enter a valid statement")

        elif tbc == 1 and tco == 2:

            val1 = float(input("enter value in degree celsius "))

            ans1 = (val1*9/5)+32

            print(ans1)
        
        elif tbc == 2 and tco == 1:

            val1 = float(input("enter value in degree celsius "))

            ans1 = (val1-32)*5/9

            print(ans1)


        

        









































































































