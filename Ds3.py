import fractions

def reduction_fraction(fraction: list[int, int]):
    i = 2
    if fraction[0] < fraction[1]:
        x = fraction[0]
    else:
        x = fraction[1]
    while i <= x:
        if fraction[0] % i == 0 and fraction[1] % i == 0:
            fraction[0] = fraction[0] / i
            fraction[1] = fraction[1] / i
            continue
        i += 1
    return [int(fraction[0]), int(fraction[1])]

def sum_fractions(list_f1, list_f2):
    if int(list_f1[1]) == int(list_f2[1]):
        result = [int(list_f1[0]) + int(list_f2[0]), int(list_f1[1])]
    else:
        nok = int(list_f1[1]) * int(list_f2[1])
        result = [int(list_f1[0]) * int(list_f2[1]) + int(list_f2[0]) * int(list_f1[1]), nok]
    return result

def multi_fractions(list_f1, list_f2):
    multi_numerator = int(list_f1[0]) * int(list_f2[0])
    multi_denominator = int(list_f1[1]) * int(list_f2[1])
    return [multi_numerator, multi_denominator]

def get_fraction():
    fraction = None
    while True:
        try:
            fraction = str(input("Введите дробь a/b: "))
            s = "/"
            if s in fraction:
                fraction = fraction.split('/')
                break
            else:
                raise Exception()
        except Exception as e:
            print(e)
            print("!! Введено не верное значение, попробуйте ещё раз !!\n")
    return fraction

list_f1 = get_fraction()
list_f2 = get_fraction()

f1 = f"{list_f1[0]}/{list_f1[1]}"
f2 = f"{list_f2[0]}/{list_f2[1]}"

list_res_sum = reduction_fraction(sum_fractions(list_f1, list_f2))
list_res_multi = reduction_fraction(multi_fractions(list_f1, list_f2))

print('\nРешение:')
print(f'{f1} + {f2} = {list_res_sum[0]}/{list_res_sum[1]}')
print(f'{f1} * {f2} = {list_res_multi[0]}/{list_res_multi[1]}')

print('\nПроверка с помощью модуля "fractions":')
fraction1 = fractions.Fraction(int(list_f1[0]), int(list_f1[1]))
fraction2 = fractions.Fraction(int(list_f2[0]), int(list_f2[1]))
print(f'{f1} + {f2} = {fraction1 + fraction2}')
print(f'{f1} * {f2} = {fraction1 * fraction2}')