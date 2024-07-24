def find_discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b ** 2 - 4 * a * c


def quadratic_equation_solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    D = find_discriminant(a, b, c)
    if D < 0:
        return "корней нет"
    elif D == 0:
        return -b / (2 * a)
    elif D > 0:
        D = D ** 0.5
    return (-b + D) / (2 * a), (-b - D) / (2 * a)


if __name__ == '__main__':
    """
    -3.0 -5.0
    12.0 1.0
    3.5
    корней нет
    """
    quadratic_equation_solution(1, 8, 15)
    quadratic_equation_solution(1, -13, 12)
    quadratic_equation_solution(-4, 28, -49)
    quadratic_equation_solution(1, 1, 1)