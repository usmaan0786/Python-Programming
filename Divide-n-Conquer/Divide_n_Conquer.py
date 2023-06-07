def divide_conquer_mul(num1 , num2):
    
    #base Case for Reccursion
    
    if len(str(num1)) == 1 or len(str(num2)):
        return num1 * num2
    
    #length of the multiplier & multiplicand
    num1 = str(num1)
    num2 = str(num2)
    len_num1 = len(num1)
    len_num2 = len(num2)
    
    
    # ...and their 'ceil' halves used for combining parts
    nby2 = len_num1//2 + 1 if len_num1 % 2 == 1 else len_num1//2
    mby2 = len_num2//2 + 1 if len_num2 % 2 == 1 else len_num2//2
    
    # halving multiplier and multiplicand into a,b and c,d...this where we are getting the pairs
    #   using 'floor' halves of lengths
    a , b = num1[ : len_num1 // 2] , num1[len_num1 // 2 : ]
    c , d = num2[ : num2 // 2] , num2[num2 // 2 : ]
    
    # recursively multiply ac, ad, bc and bd...this is where we multiply 
        #the pairs form from the step above
    ac , ad = divide_conquer_mul(int(a) , int(c)) , divide_conquer_mul(int(a) , int(d))
    bc , bd = divide_conquer_mul(int(b) , int(c)) , divide_conquer_mul(int(b) , int(d))
    
    
     # combine adding zeros and return.... this is where summation addition of zeros occur
    summation = ac * 10**(nby2 + mby2)
    summation += ad * 10**(nby2)
    summation += bc * 10**(mby2)
    summation += bd
    
    return summation
    
    

if __name__ == "__main__": 
    
    x = divide_conquer_mul(3, 6)
    print(x)