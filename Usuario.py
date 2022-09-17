class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.hacer_deposito = 0
        self.hacer_retiro = 0
        self.mostrar_balance_usuario = 0

#Depósitos
    def depositos(self, monto_dep):
        self.hacer_deposito += monto_dep
        return self

#Retiros
    def retiros(self, monto_retiros):
        self.hacer_retiro += monto_retiros
        return self

#Balance
    def balance(self):
        self.mostrar_balance_usuario = self.hacer_deposito - self.hacer_retiro
        print(self.mostrar_balance_usuario)
        return self