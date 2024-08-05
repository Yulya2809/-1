my_dict = {'Mash': 2015, 'Petya': 2017, 'Kira': 2020}
print(my_dict)
print(my_dict['Petya'])
print(my_dict.get('Anton'))
my_dict.update({'Anton': 2005,
                'Alex': 2010})
print(my_dict)
a = my_dict.pop('Petya')
print(a)
print(my_dict)

my_set = {1, 2, 'bob', False, 2, 'bob'}
print(my_set)
my_set.add((1, 2, 3))
my_set.add('pen')
my_set.remove('bob')
print(my_set)