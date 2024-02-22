emp_tpl = ()
sis_tpl = ('gina', 'michele', 'francine', 'angeala')
bro_tpl = ('joe', 'michael')
siblings = sis_tpl + bro_tpl
print(siblings)
"""to join tuples, tuple must have more than 1 value"""
"""or it has to be declared differently?"""
print(len(siblings))
lst_tpl = list(siblings)
family_members = lst_tpl.append('Keith') 
lst_tpl.append('Glory')
back_to = tuple(lst_tpl)
print(back_to)

whoknows = ' '.join(back_to)
print(whoknows)


fruitstup = ('apple', 'orange', 'andbanana')
veggietup = ('edanamme', 'corn', 'potatoisaveggiedebateawall')
animal = ('cow', 'chicken', 'pig')
food_stuff_tp = fruitstup + veggietup + animal
print(food_stuff_tp)
nowalist = list(food_stuff_tp)
middle = len(nowalist) // 2
miditem = nowalist[middle - 1 : middle + 2] if len(nowalist) % 2 == 1 else nowalist[middle - 1 : middle + 1]
print(miditem)

firsthree = nowalist[:3]
lastthree = nowalist[-3:]

del food_stuff_tp
