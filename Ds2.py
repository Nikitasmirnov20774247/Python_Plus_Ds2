hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
            5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
            10: 'a', 11: 'b', 12: 'c',13: 'd', 14: 'e', 15: 'f'}

def hex_number(num):
    hex_num = ''
    while(num > 0):
        remainder = num % 16
        hex_num = hex_dict[remainder] + hex_num
        num = num // 16
    return hex_num

def get_num():
    num = None
    while True:
        try:
            num = int(input("Введите целое положительное число: "))
            if num <= 0:
                raise Exception()
            break
        except Exception as e:
            print(e)
            print("!! Введено не верное значение, попробуйте ещё раз !!\n")
    return num

user_num = get_num()
print(f"1) Шестнадцатиричное представление числа {user_num} = {hex_number(user_num)}")
print(f"2) Шестнадцатиричное представление числа {user_num} = {hex(user_num)}")