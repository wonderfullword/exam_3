# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания!!!!!!
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания

class Tomato:
    states={0:"flower",1:"not_ripe",2:"ripe"}

    def __init__(self,index):
        self._index=index
        self._state=0


    def grow(self):
        if self._state<2:
            self._state+=1
            print("Вы находитесь на стадии", Tomato.states[self._state])
        else:
            print("Помидор дозрел")

    def is_ripe(self):
        if self._state==2:
            return True
        return False

# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая


class TomatoBush:
    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num )]


    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()


    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])


    def give_away_all(self):
        self.tomatoes = []



#
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) name - передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
#     Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.


class Gardener:
    def __init__(self,name,plant):
        self.name=name
        self._plant=plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print("Помидоры еще не дозрели")

    @staticmethod


    def knowledge_base():
        print("Садоводство-отрасль растениеводства, "
              "занимающаяся возделыванием многолетних "
              "плодовых или ягодных культур для получения фруктов, ягод.")


# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай

if __name__ == '__main__':
    Gardener.knowledge_base()
    vetka = TomatoBush(1)
    gardener = Gardener("Mark", vetka)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
