def name_shuffler(str_):
    return ' '.join([val for val in str_.split(' ')[::-1]])


print(name_shuffler("john McClane"))