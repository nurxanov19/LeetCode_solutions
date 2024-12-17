def name_shuffler(str_):
    return ' '.join(str_.split()[::-1])

print(name_shuffler('McConigan John'))