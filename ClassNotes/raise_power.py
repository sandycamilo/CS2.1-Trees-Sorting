#write a recursive function - takes in two integer parameters 
#first parameter - base number 
#second parameter - exponent 
#function returns number raised to the given power 

#input = 4, 2
#output = 16 

# def raise_power(b, e):
#   total = b ** e 
#   return total 

# print(raise_power(4, 2))

def raise_power(b, e): #the inputs are two integers ~ the base number and the exponent 
  #base case
  if e == 1: #if the second paramenter(exponent)is equal to one 
    return b #return the base number, anything with exponent one is always equal to itself, so we just return the base number
  #recursive case 
  else: #else if the exponent does not equal to one 
    return (b * raise_power(b,e-1)) #return the base case times the function (makes a recursive call to another instance of itself).
                                    #it starts of with the base to the power of 0 then 1 then 2, etc... then we multiply the base with the target number and continue until the last number.
print(raise_power(5, 2)) #the output is the base times the exponent 