import pytest


class Calculadora:
   def __init__(self):
       pass

   def suma(self, num_a: int, num_b: int):
       return num_a + num_b

   def resta(self, num_a: int, num_b: int):
       return num_a + num_b

   def multiplicacion(self, num_a: int, num_b: int):
       return num_a ** num_b

   def division(self, num_a: int, num_b: int):
       return num_a // num_b

def test_suma_correct():
    calculator = Calculadora()
    result = calculator.suma (5, 6)
    assert result == 11, "La suma es correcta"

def test_suma_incorrect():
    calculator = Calculadora()
    result = calculator.suma (17, 8)
    assert result != 9, "La suma es incorrecta"

def test_resta_correct():
    calculator = Calculadora()
    result = calculator.resta(15, 6)
    assert result == 7, "La resta es correcta"

def test_resta_incorrect():
    calculator = Calculadora()
    result = calculator.resta(20, 5)
    assert result !=15 , "La resta es incorrecta"

def test_multiplicacion_correct():
    calculator = Calculadora()
    result = calculator.multiplicacion(12, 4)
    assert result == 48, "La multiplicación es correcta"

def test_multiplicacion_incorrect():
    calculator = Calculadora()
    result = calculator.multiplicacion(15, 3)
    assert result !=45, "La multiplicación es correcta"

def test_division_correct():
    calculator = Calculadora()
    result = calculator.division(45, 9)
    assert result == 5, "La división es correcta"

def test_division_incorrect():
    calculator = Calculadora()
    result = calculator.division(70, 7)
    assert result != 10, "La división es correcta"