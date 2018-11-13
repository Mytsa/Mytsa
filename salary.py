import tax
import low_hour
import money_bonus

st = float(input('ставка: '))
hour = float(input('кількість робочих годин в місяці: '))
whour = float(input('кількість відпрацьованих годин: '))
over = float(input('кількість понаднормових годин: '))
pover = float(input('сума понаднормових премій: '))
prysut = float(input('сума премії за присутність: '))
dodat = float(input('премія до ставки % : '))
minus = float(input('виплати перед з/п(відпусні, аванс): '))
dodat = dodat / 100

if over > 0:
  second = tax.Tax.stav(money_bonus.Bonus.prem(st, hour, over, pover, prysut, dodat)) - minus
  print(second)
elif hour > whour:   # якщо відпрацював менше годин
   print(tax.Tax.stav(low_hour.Low_h.low_hour(st, hour, prysut, dodat, whour)) - minus)
else:
  st2 = (st + (st * dodat)) + prysut   # рахує з/п з вирахуваними податками
  print(tax.Tax.stav(st2) - minus)

print("різниця робочих годин згідно норми: ")
print(int((whour - hour) + over))
