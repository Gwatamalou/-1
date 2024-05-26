my_dict = {"Joan": 27, "Alex": 7, "Diana": 33}
my_set = {1, 2, 3, 'c', 4, False, 3, 'c', False, 2}

print(my_dict, my_dict.get("Joan"), my_dict.get("Mark", "no such key"), sep='\n')
my_dict.update({"Miki": 14, "karl": 25})
print(my_dict.pop("Alex"), my_dict, sep='\n')

print(my_set)
my_set.update('a', 'b')
my_set.discard(False)
print(my_set)


