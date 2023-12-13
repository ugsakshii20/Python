def sum_of_n_numbers(n):
    sum=0
    for i in range (1,n+1):
        sum +=i
    return sum

n=int(input("Enter the number"))
print("Sum is:",sum_of_n_numbers(n))
