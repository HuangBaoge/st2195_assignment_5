#def is_divisible_by_k(x, k):
#    '''
#    Checks whether x is divisible by k.
#    '''
#    assert x%k == 0 # This is used for degubbig

def is_divisible_by_k(x,k):
    '''
    Checks whether x is divisible by k.
    '''
    return x%k == 0
print(is_divisible_by_k(4,2.5))

#'''
#Store all the integers that are multiples of 2 or 5 or 7 
#that are lower or equal to 1000 (excluding doubles)
#'''
#x = ()   # should use a list
#for i in range(1000): # current range is 0 to 999
#    if (is_divisible_by_k(x, 2) & is_divisible_by_k(x, 3)) |  # it should be is_divisible_by_k(i, 2) 
#        is_divisible_by_k(x, 7):                              # should use | 
#    x.append(i)                                               # wrong indentation
    
#'''
#Sum all the integers that are multiples of 2 or 5 or 7 
#that are lower or equal to 1000 (excluding doubles)
#'''
#sum(x)


'''
Store all the integers that are multiples of 2 or 5 or 7 
that are lower or equal to 1000 (excluding doubles)
'''

list = []
for i in range(1,1000+1):
    if (is_divisible_by_k(i,2) | is_divisible_by_k(i,5) | is_divisible_by_k(i,7) ):
        list.append(i)

'''
Sum all the integers that are multiples of 2 or 5 or 7 
that are lower or equal to 1000 (excluding doubles)
'''
sum(list)
