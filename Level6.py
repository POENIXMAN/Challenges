def RemoveOddIndex(str) -> str:
    
    result = "" 
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result

str='''Tdhsi3sv aegxdekrsctihsder hsjeicyrredts ewtoyrhdf eissa wh4urnygureyw dkg 
eheypi yi7ty rfeowrf gljaytterre'''
x = RemoveOddIndex(str)
print(x)