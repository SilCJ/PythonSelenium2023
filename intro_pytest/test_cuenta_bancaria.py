import pytest


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueErro("No tienes suficientes fondos")
        self.saldo -= cantidad

    def consultar_saldo(self):
        print(f"Saldo:  {self.saldo}")
        return self.saldo

class TestCuentaBancaria:

    def setup_method(self):
        self.cuenta = CuentaBancaria("Silvia CJ", 100)

    def test(self):
        self.cuenta.retirar(80)
        assert self.cuenta.consultar_saldo() == 20, "El saldo debe ser 20 despues de retirar 90"


