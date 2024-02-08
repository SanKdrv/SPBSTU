# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Candy:
    """
        Создание и подготовка к работе объекта "Конфета"

        :param cost: Объем стакана
        :param taste_rate: Объем занимаемой жидкости
        :param is_sale: Наличие скидки

        Примеры:
        >>> candy = Candy(4, 8, True)  # инициализация экземпляра класса
    """
    def __init__(self, cost: float, taste_rate: int, is_sale: bool):
        if not isinstance(cost, (int, float)):
            raise TypeError("Цена конфеты должна быть типа int или float")
        elif cost <= 0:
            raise ValueError("Неправильная цена")
        self.price = cost
        if not isinstance(taste_rate, int):
            raise TypeError("Оценка конфеты должна быть типа int")
        elif taste_rate < 0 or taste_rate > 10:
            raise ValueError("Неправильная оценка")
        self.rate = taste_rate
        if not isinstance(is_sale, bool):
            raise TypeError("Наличие скидки на конфету должно быть типа bool")
        self.is_sale = is_sale

    def is_candy_good(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> candy = Candy(1, 6, False)
        >>> candy.is_candy_good()
        """
        ...

    def change_the_price(self, cost: float) -> None:
        """
        Изменение цены
        :param cost: Сумма добавляемая к цене

        :raise TypeError: Неправильно подобран тип переменной
        :raise ValueError: Отрицательная сумма

        Примеры:
        >>> candy = Candy(1, 6, False)
        >>> candy.change_the_price(52.213)
        """
        if not isinstance(cost, (int, float)):
            raise TypeError("Новая сумма должна быть типа int или float")
        if cost < 0:
            raise ValueError("Новая сумма должна положительным числом")
        self.price = cost
        ...

    def change_sale_mode(self, sale: float) -> None:
        """
        Изменение скидки

        :param sale: Наличие скидки
        :raise TypeError: Неправильно подобран тип переменной

        Примеры:
        >>> candy = Candy(1, 6, False)
        >>> candy.change_sale_mode(True)
        """
        if not isinstance(sale, bool):
            raise TypeError("Наличие скидки на конфету должно быть типа bool")
        self.is_sale = sale
        ...


class User:
    """
        Создание и подготовка к работе объекта "Пользователь"

        :param name: Имя польователя
        :param is_married: Состоит ли в браке пользователь
        :param id_: айди пользователя

        Примеры:
        >>> user1 = User("Alex", True, 321312)  # инициализация экземпляра класса
    """
    def __init__(self, name: str, is_married: bool, id_: int):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа string")
        elif (len(name) != 0 and name[0].islower()) or (len(name) == 0):
            raise ValueError("Неправильное имя")
        self.name = name
        if not isinstance(is_married, bool):
            raise TypeError("Наличие брака должно быть типа bool")
        self.marriage = is_married
        if not isinstance(id_, int):
            raise TypeError("ID должно быть типа int")
        if id_ < 0:
            raise ValueError("Неправильное id")
        self.id = id_

    def change_name(self, new_name: str) -> None:
        """
        Метод меняет имя пользователя

        :param new_name: Новое имя польователя
        :raise TypeError: Неправильно подобран тип переменной
        :raise ValueError: Неправильно введено имя

        Примеры:
        >>> user1 = User("Dima", False, 12341)
        >>> user1.change_name("Vasiliy")
        """
        if not isinstance(new_name, str):
            raise TypeError("Новое имя должно быть типа string")
        elif (len(new_name) != 0 and new_name[0].islower()) or (len(new_name) == 0):
            raise ValueError("Неправильное новое имя")
        self.name = new_name
        ...

    def is_user_married(self) -> bool:
        """
        Функция которая проверяет состоит ли пользователь в браке

        :return: Cостоит ли пользователь в браке

        Примеры:
        >>> user1 = User("Dima", False, 12341)
        >>> user1.is_user_married()
        """
        ...

    def return_name(self):
        """
        Метод который возвращает имя пользоваетля

        :return: Имя пользователя

        Примеры:
        >>> user1 = User("Dima", False, 12341)
        >>> name = user1.return_name()
        >>> user1.return_name()
        'Dima'
        """
        ...
        return self.name


class Car:
    """
        Создание и подготовка к работе объекта "Машина"

        :param model: Имя модели
        :param tire_pressures: Давление в шинах
        :param id_: Aйди машины

        Примеры:
        >>> mercedes = Car("a63", [1.1, 23, 4.2, 312], "EK111X77")  # инициализация экземпляра класса
    """
    def __init__(self, model: str, tire_pressures: [float], id_: str):
        if not isinstance(model, str):
            raise TypeError("Имя должно быть типа string")
        elif len(model) == 0:
            raise ValueError("Неправильное имя")
        self.name = model
        if not isinstance(tire_pressures, list):
            raise TypeError("tire_pressures должно быть типа list")
        if len(tire_pressures) != 4:
            raise ValueError("Заполните массив корректно")
        elif not isinstance(tire_pressures[0], (int, float)):
            raise ValueError("Давление в шинах должно быть типа float || int")
        self.tire_pressures = tire_pressures
        if not isinstance(id_, str):
            raise TypeError("ID должно быть типа str")
        if len(id_) == 0 or len(id_) > 8:
            raise ValueError("Неправильное id")
        self.id = id_

    def change_car_id(self, new_id: str) -> None:
        """
        Метод меняет id машины

        :param new_id: Новое id машины
        :raise TypeError: Неправильно подобран тип переменной
        :raise ValueError: Неправильно введено id

        Примеры:
        >>> bmw = Car("m7", [2.1, 23.1, 4.2, 312], "YM223X10")
        >>> bmw.change_car_id("EK322X77")
        """
        if not isinstance(new_id, str):
            raise TypeError("new_id должно быть типа str")
        if len(new_id) == 0 or len(new_id) > 8:
            raise ValueError("Неправильное new_id")
        self.id = new_id
        ...

    def change_wheel_pressure(self, wheel: int, new_pressure: float) -> None:
        """
        Метод меняет значение давления колеса машины

        :param wheel: Номер колеса
        :param new_pressure: Давление
        :raise TypeError: Неправильно подобран тип переменной
        :raise ValueError: Неправильно введено значение

        Примеры:
        >>> bmw = Car("m7", [2.1, 23.1, 4.2, 312], "YM223X10")
        >>> bmw.change_wheel_pressure(1, 1.2345)
        """
        if not(isinstance(wheel, int)):
            raise TypeError("wheel должно быть типа int")
        if not(1 <= wheel < 5):
            raise ValueError("Неправильный индекс колеса")
        if not(isinstance(new_pressure, (int, float))):
            raise TypeError("new_pressure должно быть типа int || float")
        if new_pressure < 0:
            raise ValueError("Неправильное новое давление")
        self.tire_pressures[wheel - 1] = new_pressure
        ...

    def break_wheel(self, wheel_id: int) -> None:
        """
        Метод меняет значение давления колеса машины на 0

        :param wheel_id: Номер колеса
        :raise TypeError: Неправильно подобран тип переменной
        :raise ValueError: Неправильно введено значение

        Примеры:
        >>> bmw = Car("m7", [2.1, 23.1, 4.2, 312], "YM223X10")
        >>> bmw.break_wheel(2)
        """
        if not(isinstance(wheel_id, int)):
            raise TypeError("wheel должно быть типа int")
        if not(1 <= wheel_id < 5):
            raise ValueError("Неправильный индекс колеса")
        self.tire_pressures[wheel_id - 1] = 0
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
