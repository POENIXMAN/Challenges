def reverseString(str) -> str:
    
    str = str[::-1]
    return str

line = 'erutuf eht ni ti deen lliw uoy drow siht peek namretaw si deen lliw uoy drow terces eht'
result = reverseString(line)
print(result)