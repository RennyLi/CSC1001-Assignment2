number=input("Please enter your credit card number:")  # prompt up the user to enter the credit card number

def sum_of_double_even_place(number):  # define a function to calculate the sum of double even place from step 2
    sum_double=0  # at first the sum up value is zero
    for i in number[-2:-len(number)-1:-2]:  # get every value in the even place from right to left
        t=2*int(i)  # convert from string type to integer type
        if t > 9:  # if the number is two-digit long
            t=t//10+t%10  # add up the two digits to get a single-digit number
        sum_double+=t  # sum up the double even place number
    return sum_double  # return the result

def sum_of_odd_place(number):  # define a function to return sum of odd place digits in number
    sum_up=0  # at first the sum up value is zero
    for i in number[-1:-len(number):-2]:  # get every value in odd place from right to left
        m=int(i)  # change the digit from string type to integer type
        sum_up+=m  # sum up the digits we get
    return sum_up  # return the result

def sum_of_two_steps(number):  # define a function to sum up the results from step 1 and step 2
    sum_two_steps=int(sum_of_double_even_place(number))+int(sum_of_odd_place(number))  
    return sum_two_steps

def is_valid(number):  # define a function to check whether the credit card number is valid
    if (number.startswith("4") or number.startswith("5") or number.startswith("37") or number.startswith("6")) \
        and sum_of_two_steps(number)%10 == 0 and 12 < len(number) < 17:
        print("Your credit card number is valid!")  # return true if the card number is valid
    else:
        print("Your credit card number is invalid!")

is_valid(number)  # call the function to execute the check process