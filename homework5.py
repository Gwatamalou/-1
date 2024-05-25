immutable_var = ('Тапинамбур', 14, True, [0, 1, 'c', 4])
print(immutable_var)

"""
пункт 3 задания изменитие неизменяемую колекцию...
ВЫЗОВ ПРИНЯТ!

"""

tlist = list(immutable_var)
tlist.append('easy win')
immutable_var = tuple(tlist)
print(immutable_var)

mutable_list = ['Тапинамбур', 14, True, [0, 1, 'c', 4]]
mutable_list[0], mutable_list[3][1] = 'UGU', False
print(mutable_list)