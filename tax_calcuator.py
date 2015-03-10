income = float(input("How much did you make last year? "))
agi = income - 10300
owe = 0


if agi < 9225:
    owe = agi * 0.1

if agi < 37450:
    owe += (agi - 9225) * 0.15


print(owe)

