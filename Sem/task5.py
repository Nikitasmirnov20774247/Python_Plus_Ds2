a = int(input('Введите коэффициент a: '))
b = int(input('Введите коэффициент b: '))
c = int(input('Введите коэффициент c: '))

d = b**2-4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('Корни уравнения: ', x1, x2)
elif d == 0:
    print('Корень уравнения: ', -b / (2 * a))
else:
    d = complex(b**2-4 * a * c)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('Комплексные корни уравнения: ', x1, x2)