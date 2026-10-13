Name = "Babita Sharma"
Age = 40
Summary = "I want to learn to code Python!"

print(Name, Age, Summary)
print('Happy New Year!')
print()

##Babita - Decision making first Test code:
num=21 
    ## Type your code here 

if num%7==0:

   print (True)
   
else: 
     
   print (False)

#Babita - Data Manupulation Test code
a=10
b=3.6
c=str(a + b)

print(c) 

a=10
b=3.6
c=str(a + b)

print(c) 

print (type (c))

#Babita - decision making on last digit_Test code
 
num=27  
last_digit=num%10

if (last_digit%3)==0:       
 result=(True)

else:      
 result=(False)

print (result)

###System accepted code for "decision making on last digit" Test code

def main():  

  

    num=27  
    last_digit=num%10

    ## Type your code here  
    if (last_digit%3)==0:

       divisible=True

    else:   
        
      divisible=False
      
    #################### 
    return divisible
  

print (main())