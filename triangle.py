import sys

def check_triangle(sides: list) -> str:
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a + b  <= c) | (a + c <= b) | (b + c <= a):
        return "Таких треугольников не существует: несоответствие длин сторон правилу треугольника"
    elif (a == 0) | (b ==0) | (c == 0):
        return "Неправильный треугольник: сторона не может иметь нулевую длину"
    elif (a == b) & (b == c) & (c == a):
        return "Равносторонний треугольник"
    elif (a == b) | (b == c) | (c == a):
        return "Равнобежренный треугольник"
    else:
        return "Обычный треугольник"
    
    
if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Ошибка ввода данных: у треугольника 3 стороны")
        sys.exit()

    for s in sys.argv[1:]:
        if s.isalpha() | int(s) <= 0:
            print("Ошибка! Длина строны должна быть положительным числом!")
            sys.exit()
    
    sides = [eval(sa) for sa in sys.argv[1:]]

    print(check_triangle(sides))