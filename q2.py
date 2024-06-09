def reverse(number):  # define a function to take reverse number
    reverse_number=""  # first set reverse number as an empty string
    while number != 0:
        reverse_number+=str(number%10)  # slice the number through dividing it by 10
        number//=10  # add them together as a reverse string
    reverse_number=int(reverse_number)  # convert the string into an integer
    return reverse_number  # return the reverse number

def is_nonpalindromic_number(number):  # define a function to check if it is nonpalindromic number
    if number != reverse(number):  # if the number not equals to its reverse number
        return True  # then it is nonpalindromic
    else:
        return False  # otherwise, it's palindromic

def is_prime(number):  # define a function to check whether the number is a prime number
    divisor=2  
    while divisor <= number/2:
        if number%divisor == 0:  # if can be divided by divisor, it does not satisfy the definition of prime number
            return False  # thus it is not prime number
        else:
            divisor+=1  # go through every divisor to check whether it is indeed prime number
            continue
    return True  # if can't be divided by all divisors, then it is a prime number

def reversal_is_prime(number):  # define a function to check whether the reversal of a number is prime number
    divisor=2  # use the same method to examine whether the reverse number is prime number
    reversal=reverse(number)
    while divisor <= reversal/2:
        if reversal%divisor == 0:
            return  False
        else:
            divisor+=1
            continue
    return True

def emirp():  # define a function to check whether a number is an emirp
    count=0  # count the total number of displayed emirps
    number=13  # start from the smallest emirp number 13
    while count < 100:  # display the first 100 emirps
        if is_nonpalindromic_number(number) and is_prime(number) and reversal_is_prime(number):
            print("%6d"%number,end="")  # if satisfy all three conditions above, print it out and align them properly
            count+=1  # count it into the total number
            number+=1  # continue to check whether the next number is emirp number
        else:
            number+=1  # continue to check whether the next number is emirp number
            continue
        if count%10 == 0:  # dispaly 10 numbers per line
            print() 
emirp()  # call the emirp function to print the output