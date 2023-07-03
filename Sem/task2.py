import sys

lister = [12, 'asfd', 12.31]
qwe = {1: 'qwra', 123: 123}
ewq = (12, 42)
qwer = {13, 34, 234, 'sfsf', 23.123}
asd = frozenset([123, 42, 'afa', 34])

data = [1, 'qwe', 1.1, False, lister, qwe, ewq, qwer, asd]
lener = len(data)

for i, item in enumerate(data, start=1):
    print(f'{i} значение: {item}, адрес: {id(item)}, размер: {sys.getsizeof(item)}')
    if isinstance(item, int) and item > 0:
        print('Является положительным целым числом')
    if isinstance(item, str):
        print('Является строкой')
    try:
        print(f'{hash(item)}, + это хэш')
    except:
        pass