def leapYearCheck() -> None:
    #Checks if the year is a leap year
    year = int(input('Enter the year you want to check : \n'))
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:   
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

leapYearCheck()