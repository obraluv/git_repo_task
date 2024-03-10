def number_to_check(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime =False
            
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

n = int(input("Enter a number to check:"))
number_to_check(n)