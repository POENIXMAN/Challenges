def multTable() -> None:
    
    for row in range(1, 11):
        print(*(f"{row*col:3}" for col in range(1, 11)))
            
multTable()