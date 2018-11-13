#print ("== Школьная группа по рисованию :-) ===\n\n\n")

#person = {'name' : ['Алина','Аня','Петя','Саня','Вася','Катя'],
#'age':['14','11','12','13','11','12'],
#'value':['5','4','4.6','5','3.3','4.5']
#}
#getname = input("Введите имя ученика: ")
#i = 0
#while i <= len(getname):
#    if getname == person['name'][i]:
#        print(person['name'][i],person['age'][i],person['value'][i])
#        i += 1
#
#        break
#   elif getname != person['name'][i]:
#        print("Такого ученика нет!")



school = {'name' :['ivan', 'sergey', 'lena', 'pasha'], 'age' : [12, 15, 13, 16], 'average': [3, 4, 2, 5]}
# print (school['name'][0]) - Вывод какого-либо одного значения

for key, value in school.items():
	print ('В ключе - ', key, ' находятся такие значения: ', school[key])