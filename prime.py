def is_prime(n):
    if n<1:
        print(n,"number is not prime")
    for i in range(n,2):
        if n % i ==0:
            print(n,"number is not prime")
    else:
        print(n,"Number is prime")
n=int(input("Enter number"))
is_prime(n)
