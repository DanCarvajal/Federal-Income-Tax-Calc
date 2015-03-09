income = int(input("How much did you make last year? "))
agi = income - 10300

if agi > 0 and agi <= 9225:
    owe = agi * 0.1
    print("You'll owe ${} in taxes".format(owe))

elif agi > 9225 and agi <= 37450:
    owe = agi * 0.15
    print("You'll owe ${} in taxes".format(owe))

elif agi > 37450 and agi <= 90750:
    owe = agi * 0.25
    print("You'll owe ${} in taxes".format(owe))

elif agi > 90750 and agi <= 189300:
    owe = agi * 0.28
    print("You'll owe ${} in taxes".format(owe))

elif agi > 189300 and agi <= 411500:
    owe = agi * 0.33
    print("You'll owe ${} in taxes".format(owe))

elif agi > 411500 and agi <= 413200:
    owe = agi * 0.35
    print("You'll owe ${} in taxes".format(owe))

elif agi > 413200:
    owe = agi * 0.396
    print("You'll owe ${} in taxes".format(owe))

