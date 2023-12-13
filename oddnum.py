def odd_number(n):
    return [i for i in range(n*2) if i%2 !=0]

n=int(input("Enter the numbers"))
print("Odd numbers are:",odd_number(n))
