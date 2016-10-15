a, *b, c = (1, 2, 3, 4)                       
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)


"""D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])                
   ####                                               
ist(D.items())
[('a', 1), ('c', 3), ('b', 2)]
for (key, value) in D.items():
    print(key, '=>', value) """

