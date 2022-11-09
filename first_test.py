# импортируем библиотеку:
import pytest

# импортируем код тестируемого приложения Калькулятор:
# app.calculator - значит, что в папке app лежит файл calculator
from app.calculator import Calculator

# создаем класс тестируемого приложения, которые обязательно начинаются со слова Test:
class TestCalc:
    # определяем подготовительный метод setup в котором подключаем тестируемый объект
    def setup(self):
        # создаем объект калькулятора из импортируемого класса
        self.calc = Calculator

    # пишем тесты, которые обязательно начинаются со слова test
    # функция умножения (multiply), которую проверяем и результат (correctly), который она должна вернуть
    def test_multiply_calculate_correctly(self):
        # assert сравниваем ожидание с результатом
        assert self.calc.multiply(self, 2, 2) == 4

    # # добавим отрицательный тест для умножения
    # def test_multiply_calculation_failed(self):
    #     assert self.calc.multiply(self, 2, 2) == 5

    # функция деления (division) положительный тест
    def test_division_calculate_correctly(self):
        # assert сравниваем ожидание с результатом
        assert self.calc.division(self, 10, 2) == 5

    # # добавим отрицательный тест для деления
    # def test_division_calculation_failed(self):
    #     assert self.calc.division(self, 10, 2) == 2

    # функция вычитания (subtraction) положительный тест
    def test_subtraction_calculate_correctly(self):
        # assert сравниваем ожидание с результатом
        assert self.calc.subtraction(self, 100, 2) == 98

    # # добавим отрицательный тест для вычитания
    # def test_subtraction_calculation_failed(self):
    #     assert self.calc.subtraction(self, 100, 2) == 90

    # функция сложения (adding) положительный тест
    def test_adding_calculate_correctly(self):
        # assert сравниваем ожидание с результатом
        assert self.calc.adding(self, 58, 42) == 100

    # # добавим отрицательный тест для сложения
    # def test_adding_calculation_failed(self):
    #     assert self.calc.adding(self, 58, 42) == 104



# !!!!! #
# если сбоку нет зеленых маркеров, то не определяет, что запускать нужно pytest
# чтобы воспользоваться библиотекой pytest, нужно зайти в настройки:
# PyCharm/Preferences/Tools/Python Integrated Tools и в поле Testing выбрать pytest
# сбоку должны появится зеленые маркеры в виде стрелочек














