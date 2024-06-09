def sqrt(n):  # define the take square function with n as the parameter
    last_guess=eval(input("Please enter a positive number:"))  # prompt up the user to enter a number for guess
    while True:  # keep looping until finding the correct answer
        next_guess=(last_guess+(n/last_guess))/2  # use the given equation to calculate the next guess
        if -0.0001 < next_guess-last_guess < 0.0001:  # difference very small, thus claiming it's the approximated value
            print(next_guess)  # print the approximated square root of n
            break  # stop the infinite loop
        else:
            last_guess=next_guess  # we haven't found the answer, next guess becomes last guess
            continue  # the approximation process continues
def main():
    while True:
        n=eval(input("Please input a positive number that you want to take square root:"))  # Prompt up the user to enter a number
        if n <= 0:
            continue
        else:
            sqrt(n)
            break

main()
