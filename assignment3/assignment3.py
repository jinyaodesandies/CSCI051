#TODO: Write your names here
# Student 1:Jinyao DeSandies
# Student 2:Franklyn Forson

'''
    Performs the bitwise and operation on x and y
    Example: bitwise_and(6, 5) = 4
    Legal ops: ~ |
    Max ops: 8
    param x: (num)
    parm y: (num)
    return: (num) x&y
'''
def bitwise_and(x, y):
    r = ~(~x|~y) # TODO: edit this line so that r is equal to x&y but you are only allowed to use the ~ and | operators.
    return r


'''
    Performs the bitwise nor operation on x and y
    Example: bitwise_nor(6, 5) = -8
    Legal ops: ~ &
    Max ops: 8
    param x: (num)
    parm y: (num)
    return: (num) ~(x|y)
'''
def bitwise_nor(x, y):
    r = (~x&~y) # TODO: edit this line so that r is equal to ~(x|y) but you are only allowed to use the ~ and & operators.
    return r


'''
    Performs the bitwise xor operation on x and y
    Example: bitwise_xor(4, 5) = 1
    Legal ops: ~ &
    Max ops: 14
    param x: (num)
    parm y: (num)
    return: (num) x^y
'''
def bitwise_xor(x, y):
    a = (~x & y);b = (x & ~y); r = ~(~a & ~b) # TODO: edit this line so that r is equal to x^y but you are only allowed to use the ~ and & operators.
    return r


'''
    Checks whether x and y are equal
    Example: are_equal(5, 5) = 1, are_equal(4, 5) = 0
    Legal ops: ~ ^ | + << >> !=
    Max ops: 5
    param x: (num)
    parm y: (num)
    return: (num) 1 if x==y, 0 otherwise
'''
def are_equal(x, y):
    r = ((x^y) != 0)^1

# TODO: edit this line so that r is equal to 1 if x and y are equal and 0 otherwise. You cannot use if/else statements. You can only use the operators ~ & ^ | + << >> !=
    return r


'''
    Negates x
    Example: negate(47) = -47, negate(-47) = 47, negate(0) = 0
    Legal ops: ~ & ^ | + << >>
    Max ops: 5
    param x: (num)
    return: (num) -x
'''
def negate(x):
    r = ~x+1 # TODO: edit this line so that r is equal to -x. You cannot use if/else statements. You can only use the operators ~ & ^ | + << >>
    return r


'''
    Checks whether x is even
    Example: is_even(47) = 0, is_even(48) = 1
    Legal ops: ~ & ^ | + << >>
    Max ops: 5
    param x: (num)
    return: (num) 1 if x is even, 0 otherwise
'''
def is_even(x):
    r = (x&1)^1 # TODO: edit this line so that r is equal to 1 if x is even 0 otherwise. You cannot use if/else statements. You can only use the operators ~ & ^ | + << >>
    return r


'''
    Returns the absolute value of x
    Example: absolute(-47) = 47, absolute(47) = 47, absolute(0) = 0
    Legal ops: ~ & ^ | + << >> != bit_length()
    Max ops: 10
    param x: (num)
    return: (num) abs(x)
'''
def absolute(x):
    
    sign=x>>x.bit_length();r = (x^sign)+(sign&1) # TODO: edit this line so that r is equal to the absolute value of x. You cannot use if/else statements. You can only use the operators ~ & ^ | + << >> !=
    return r

'''
    Isolates the least significant set bit, that is the right-most bit that is set to 1 in the binary representation.
    Example: least_significant_bit(48) = 16, because 48 in binary is 110000 and the 4th bit being the right-most 1 corresponds to 2^4=16.
    Similarly, least_significant_bit(-384) = 128, because -384 in two's complement is 1010000000 and the 7th bit being the right-most 1 corresponds to 2^7=128
    Legal ops: ~ & ^ | + << >> !=
    Max ops: 10
    param x: (num)
    return: (num) isolates the least significant set bit and returns its index as power of 2
'''
def least_significant_bit(x):
    r = x&(~x+1)
    # TODO: edit this line so that r is equal to the least significant set bit and returns its index as power of 2
    return r


# Provided tests
'''print(bitwise_and(6,5)) #should print 4
print(bitwise_nor(6,5)) #should print -8
print(bitwise_xor(4,5)) #should print 1
print(are_equal(9,5)) #should print 0
print(negate(-47)) #should print 47
print(is_even(47)) #should print 0
print(absolute(-47)) #should print 47
print(least_significant_bit(44)) #should print 4
'''

# TODO Write at least one more print statement per function to test your code
"""print(bitwise_and(2,5)) #should print 2
print(bitwise_nor(3,5)) #should print 2
print(bitwise_xor(4,5)) #should print 2
print(are_equal(2,5)) #should print 0
print(negate(47)) #should print -47
print(is_even(48)) #should print 1
print(absolute(47)) #should print 47
print(least_significant_bit(5)) #should print 1"""