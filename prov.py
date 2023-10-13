#Author: Axel Edsbagge
#Date.   2023-10-13

welcome = str(print('Ei22 - praktiskt prov ht23'))

def calc_para(parallel):
    acc = 0
    for value in parallel:
        acc += 1/value
        
    return 1/acc 

def calc_serie(serie):
    acc = 0
    for value in serie:
        acc += value
    return acc


value = ''


value = input('Resistor storlek: ')
value.split()
my_list = [int(value) for value in value.split()]

if value == '':
    print('Serieresistans: 0')
    print('Parallellresistans: 0')
else:
    print(f'Serieresistans: {calc_serie(my_list)}')
    print(f'Parallellresistans: {calc_para(my_list)}')

