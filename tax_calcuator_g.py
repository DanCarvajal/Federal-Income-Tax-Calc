ncome = float(input("How much did you make last year? "))
agi = income - 10300
owe = 0
brackets = [0,9225,37450,65000]
rates = [0,0.1,0.15,0.25]
n=1
lim = len(brackets)

while True:
   if agi < brackets[n]:
       owe += (agi-brackets[n-1]) * rates[n]
       break
   else:
       owe += brackets[n]*rates[n]
   n=n+1
   
   if n==lim-1:
       owe += (agi-brackets[n-1]) * rates[n]
       break

print(owe)