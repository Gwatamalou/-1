my_string = input('Enter your text: ')
while not my_string:
    my_string = input('Enter your text: ')
print(len(my_string), my_string.upper(), my_string.lower(), my_string.replace(' ',''), my_string[0], my_string[-1], sep='\n')
