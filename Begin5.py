try:
    a = int(input("Введите длину ребра a: "))
    V = a ** 3
    S = 6 * (a ** 2)
    print(f"Обьем равен: {V}")
    print(f"Площадь поверхности равна {S}")
except:
    print("Неверно")

