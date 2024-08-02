immutable_var = (1, 'box', True)
print(type(immutable_var))
print(immutable_var)
# immutable_var[0] = 5  # нельзя изменить, потому что, кортежи неизменямые объекты
print(immutable_var)

mutable_list = [1,2,3,4]
print(mutable_list)
mutable_list[2] = 'run'
print(mutable_list)