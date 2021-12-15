def isPerfectNumber(n):

    perfect_sum = 0
    
    for i in range(1,n):
        if n % i == 0:
            perfect_sum += i

    return perfect_sum == n

number = int(input('Enter number: '))

if isPerfectNumber(number):
    print(f'{number} is PERFECT')
else:
    print(f'{number} is NOT PERFECT')   