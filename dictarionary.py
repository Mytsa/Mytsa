S = {'name': ['Spencer', 'Monica', 'Roman', 'Botan'], 'years old': [14, 12, 15, 16], 'middle assessment': [11, 11, 12, 7]}

#name = ['Spencer', 'Monica', 'Roman', 'Botan']
#years_old = [14, 12, 15, 16]
#middle_assessment = [11, 11, 12, 7]


getname = input("input name: ")
i = S.index(getname, [0 [ 4]])
for key, value in S['name'][i]:
    print(S['name'][i], S['years old'][i], S['middle assessment'][i])




#i = S.index(getname, [0 [ 4]])

#i = name.index(getname, [0 [len(getname)]]) # треба витягти ідекс під яким сидить введене імья

#while i<= len(getname):
#if getname == S['name'][i]:
#    print(S['name'][i], S['years old'][i], S['middle assessment'][i])


#elif getname != S['name'][i]:
#    print("uncorrect name")
#    i += 1


#dict.setdefault(key, default)