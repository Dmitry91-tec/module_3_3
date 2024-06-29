def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(3, 'СТРОКА', False)
values_list = ['string', True, 7]
values_dict = {'a': False, 'b': 9, 'c': 'слово'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [True, 'NFS']
print_params(*values_list_2, 42)