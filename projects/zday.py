def main():
    print(" This is a monthly payment loan calculator ")
    print("")

    principal = float(input("Input loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years: "))

    monthly_int_rate = apr / 1200
    no_of_months = years * 12
    monthly_pay = principal * monthly_int_rate / (1 -(1 + monthly_int_rate) ** (-no_of_months))

    print(" The monthly payment for this loan is: %.2f " % monthly_pay)

#
s = "   fly me   to   the moon  "
print(s.split())


word=s.split()
print(len(word[-1]))
print(list(range(5, 5+1, 6)))

z = 'AAAABBBCCDAABBB'
print(list(z))

print(z.isdigit())

