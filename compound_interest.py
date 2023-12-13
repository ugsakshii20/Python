def calculate_compound_interest(principal,rate,time):
    amount=principal*(1+rate/100)**time
    compound_interest=amount-principal
    return compound_interest

principal=float(input("Enter principle:"))
rate=float(input("Enter rate of interest(%):"))
time=float(input("Enter time (in years):"))

compound_interest=calculate_compound_interest(principal,rate,time)
print("Compount Interest is:",compound_interest)
