if __name__ == "__main__":
    class Country:
        """
            Базовый класс Страна

            :param name_of_country: Название страны
            :param number_of_people: Количество населения
            :param leader: Имя президента

            Примеры:
            >>> Russia = Country("Россия", 7042300423, "В.В. Путин")  # инициализация экземпляра класса

        """
        def __init__(self, name_of_country: str, number_of_people: int, leader: str) -> None:
            """
            Конструктор класса Country

            :param name_of_country: Название страны
            :param number_of_people: Количество населения
            :param leader: Имя президента

            Примеры:
            >>> Country("Россия", 7042300423, "В.В. Путин")
            """
            self.name_of_country = name_of_country
            self._number_of_people = number_of_people
            self.leader = leader
            self._happiness = 0

        def __repr__(self) -> str:
            """
            Метод для отображения информации об объекте класса для разработчиков
            Примеры:
            >>> USA = Country("USA", 212332451, "Biden")
            >>> USA.__repr__()
            """
            return f"{self.__class__.__name__}(name_of_country={self.name_of_country!r}, " \
                   f"number_of_people={self.number_of_people!r}," \
                   f" leader={self.leader!r})"

        def __str__(self) -> str:
            """
            Метод для отображения информации об объекте класса для пользователей
            Примеры:
            >>> USA = Country("USA", 212332451, "Biden")
            >>> USA.__str__()
            """
            return f"Страна {self.name_of_country}. Глава {self.leader}"

        def change_leader(self, new_name: str) -> None:
            """
            Метод меняет Главу страны

            :param new_name: Новое имя Главы

            Примеры:
            >>> Russia = Country("Россия", 7042300423, "В.В. Путин")
            >>> Russia.change_leader("Кто-то")
            """
            if isinstance(new_name, str):
                self.leader = new_name
            else:
                raise TypeError("Err")

        def change_name(self, new_name: str) -> None:
            """
            Метод меняет название страны

            :param new_name: Новое название страны

            Примеры:
            >>> Russia = Country("Россия", 7042300423, "В.В. Путин")
            >>> Russia.change_name("Новое название")
            """
            if isinstance(new_name, str):
                self.name_of_country = new_name
            else:
                raise TypeError("Err")

        def make_party(self) -> str:
            """
            Метод увеличивает счастье народа и выводит благодарность правителю
            Увеличивает значение protected переменной _happiness
            _happiness protected во избежание случайных изменений извне

            Примеры:
            >>> Russia = Country("Россия", 7042300423, "В.В. Путин")
            >>> Russia.make_party()
            """
            self._happiness += 1
            return "УРА!!! " + self.leader

        @property
        def number_of_people(self) -> int:
            """
            Геттер для свойства number_of_people
            """
            return self._number_of_people

        @number_of_people.setter
        def number_of_people(self, new_num: int) -> None:
            """
            Cеттер для свойства number_of_people
            :param new_num: Новое количество жителей
            """
            if isinstance(new_num, int):
                if new_num <= 0:
                    raise ValueError("Error")
                else:
                    self._number_of_people = new_num
            else:
                raise TypeError("Error")

    class City(Country):
        """
            Дочерний класс Город от Базового класса Страна

            :param name_of_country: Название страны
            :param number_of_people: Количество населения
            :param leader: Имя президента
            :param name_of_city: Название города
            :param regional_leader: Имя регионального лидера
            :param number_of_shops: Количество магазинов

            Примеры:
            >>> Boston = City("USA", 212332451, "Biden", "Boston", "Leader", 32123)
            # инициализация экземпляра класса

        """
        def __init__(self, name_of_country: str, number_of_people: int, leader: str,
                     name_of_city: str, regional_leader: str, number_of_shops: int) -> None:
            """
            Конструктор дочернего класса City

            :param name_of_country: Название страны
            :param number_of_people: Количество населения
            :param leader: Имя президента
            :param name_of_city: Название города
            :param regional_leader: Имя регионального лидера
            :param number_of_shops: Количество магазинов

            Примеры:
            >>> City("USA", 212332451, "Biden", "Boston", "Leader", 32123)
            """
            super().__init__(name_of_country, number_of_people, leader)
            self.name_of_city = name_of_city
            self.regional_leader = regional_leader
            self.number_of_shops = number_of_shops

        def __repr__(self) -> str:
            """
            Метод для отображения информации об объекте класса для разработчиков
            Примеры:
            >>> Boston = City("USA", 212332451, "Biden", "Boston", "Leader", 32123)
            >>> Boston.__repr__()
            """
            return f"{self.__class__.__name__}(name_of_city={self.name_of_city!r}, " \
                   f"regional_leader={self.regional_leader!r}, " \
                   f"number_of_shops={self.number_of_shops!r})"

        def __str__(self) -> str:
            """
            Метод для отображения информации об объекте класса для пользователей
            Примеры:
            >>> Boston = City("USA", 212332451, "Biden", "Boston", "Leader", 32123)
            >>> Boston.__str__()
            """
            return f"Название города {self.name_of_city}. " \
                   f"Местная власть {self.regional_leader}. " \
                   f"Число магазинов {self.number_of_shops}"

        def make_party(self) -> str:
            """
            Метод увеличивает счастье народа и выводит благодарность правителю
            Перегрузка позволяет восхлавить помимо лидера страны ещё и регионального лидера
            Примеры:
            >>> Boston = City("USA", 212332451, "Biden", "Boston", "Leader", 32123)
            >>> Boston.make_party()
            """
            self._happiness += 1
            return f"YPAA!!!! {self.leader} и {self.regional_leader}"

    class Village(Country):
        """
            Дочерний класс Город от Базового класса Страна

            :param name_of_country: Название страны
            :param number_of_people: Количество населения
            :param leader: Имя президента
            :param name_of_village: Название деревни
            :param regional_departament: Название управляющей партии
            :param number_of_lakes: Количество озёр рядом

            Примеры:
            >>> Derevyanovo = Village("Belarus", 213211, "Leader", "Derevyanovo", "Управляющая организация", 2)
            # инициализация экземпляра класса

        """
        def __init__(self, name_of_country: str, number_of_people: int, leader: str,
                     name_of_village: str, regional_departament: str, number_of_lakes: int) -> None:
            """
            Конструктор дочернего класса Village

            :param name_of_country: Название страны
            :param number_of_people: Количество населения
            :param leader: Имя президента
            :param name_of_village: Название деревни
            :param regional_departament: Название управляющей партии
            :param number_of_lakes: Количество озёр рядом

            Примеры:
            >>> Village("Belarus", 213211, "Leader", "Derevyanovo", "Управляющая организация", 2)

            """
            super().__init__(name_of_country, number_of_people, leader)
            self.name_of_village = name_of_village
            self.regional_departament = regional_departament
            self.number_of_lakes = number_of_lakes

        def change_name(self, new_name: str) -> None:
            """
            Перегруженный метод позволяет поменять название деревни
            :param new_name: Новое название деревни
            Примеры:
            >>> Derevyanovo = Village("Belarus", 213211, "Leader", "Derevyanovo", "Управляющая организация", 2)
            >>> Derevyanovo.change_name("Dvuozerie")
            """
            if isinstance(new_name, str):
                self.name_of_village = new_name
            else:
                raise TypeError("Err")
