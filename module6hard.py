import math
class Figure:
    sides_count = 0
    korrect = False
    def __init__(self, color, *args):
        self.__sides = []
        self.__color = []
        for i in color: self.__color.append(i)
        if len(args) == 1:
            for i in range(1,self.sides_count+1):
                self.__sides.append(args[0])
        else:
            for i in range(0, self.sides_count):
                self.__sides.append(1)


        filled = True

    def get_color(self):
        return self.__color


    def __is_valid_color(self,r , g, b):
        if 0 <= r <=250 and 0<= g <= 250 and 0<=b<=250:
            self.korrect = True

    def set_color(self, r,g,b):
        self.__is_valid_color(r,g,b)
        if self.korrect:
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def __is_valid_sides(self):
        prover = True
        for i in self.__sides:
            if i<0:
                prover = False
                break
        if len(self.__sides) != super.sides_count:
            prover = False
        return prover

    def get_sides(self):
        return self.__sides
    def __len__(self):
        return self.__sides[0]*self.sides_count

    def set_sides(self, *new_sides):
        if len(new_sides) == len(self.__sides):
            self.__sides = []
            self.__sides.append(new_sides[0])

    # def __str__(self):
    #     print(self.__sides)
    #     print((self.__color))
class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *args):
        super().__init__(color, *args)
        # print(self.__radius())
        # print(self.get_square())

    def __radius(self):
        radius = round(super().__len__()/(2*3.14),2)
        return radius


    def get_square(self):
        square = round(3.14 * self.__radius()**2,2)
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *args):
        super().__init__(color, *args)
        print(self.get_square())

    # Площадь треугольника по формуле Герона
    def get_square(self):
        sides = super().get_sides()[0]
        p = sides*3/2
        square = math.sqrt(p *((p-sides)**3))
        return square

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *args):
        super().__init__(color, *args)

    def get_volume(self):
        sides = super().get_sides()
        return sides[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
#
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

#
# Проверка объёма (куба):
print(cube1.get_volume())