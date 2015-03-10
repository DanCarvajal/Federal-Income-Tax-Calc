income = int(input("How much did you make last year? "))
agi = income - 10300

if agi < 9225:
    owe = agi * 0.1

if agi < 37450:
    owe += agi * 0.15

if agi < 90750:
    owe += agi * 0.25

if agi < 189300:
    owe += agi * 0.28

if agi < 411500:
    owe += agi * 0.33

if agi < 413200:
    owe += agi * 0.35

if agi > 413200:
    owe += agi * 0.396

print(owe)

