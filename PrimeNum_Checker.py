def prime_checker(number): # a function to check for prime_checker is created which take in number to check as input
    prime_num = True   # a variable prime num is defined and set to True
    
    for num in range(2, number):  # this line of code iterate over the range of the number we are checking and starts from 2
    #  in order to exclude 1 and the number we are checking since a prime number is only divisible by itself and 1 only without any reminder 
        if number % num == 0:  # here, if number to check is divisible by number in the range without reminder
            prime_num = False  # that means the number we are checking is not a prime number 
            
    if prime_num:  # here if after the loop above the number to check is divisible by any number in the range with a reminder, then it is a prime number
        print(f"{number} is a prime number")  # this print statement will output
    else:  # this is basically telling us that if anything else happen, the number is not a prime number
        print(f"{number} is not a prime number")

n = int(input("Enter a number to check:"))  # a variable n is created to take in the user input
prime_checker(n)  # user input in assign to our function and function is called to enable every code created within it to run