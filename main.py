from Usuario import Usuario

Usuario1 = Usuario("Edward")
Usuario2 = Usuario("Iván")
Usuario3 = Usuario("María Elena")

#Usuario1: 3 depósitos y 1 giro, obtener balance
Usuario1.depositos(25000).depositos(25000).depositos(25000).retiros(10000).balance()

#Usuario2: 2 depósitos y 2 giros, obtener balance
Usuario2.depositos(30000).depositos(30000).retiros(15000).retiros(15000).balance()

#Usuario3: 1 depósito y 3 giros, obtener balance
Usuario3.depositos(25000).retiros(10000).retiros(10000).retiros(10000).balance()

"""#Usuario1: 3 depósitos y 1 giro, obtener balance
Usuario1.depositos(25000)
Usuario1.depositos(25000)
Usuario1.depositos(25000)
print("Total depósitos",Usuario1.nombre,":",Usuario1.hacer_deposito)
Usuario1.retiros(10000)
print("Total retiros",Usuario1.nombre,":",Usuario1.hacer_retiro)
Usuario1.balance()
print("Balance final",Usuario1.nombre,":",Usuario1.mostrar_balance_usuario)

#Usuario2: 2 depósitos y 2 giros, obtener balance
Usuario2.depositos(30000)
Usuario2.depositos(30000)
print("Total depósitos",Usuario2.nombre,":",Usuario2.hacer_deposito)
Usuario2.retiros(15000)
Usuario2.retiros(15000)
print("Total retiros",Usuario2.nombre,":",Usuario2.hacer_retiro)
Usuario2.balance()
print("Balance final",Usuario2.nombre,":",Usuario2.mostrar_balance_usuario)

#Usuario3: 1 depósito y 3 giros, obtener balance
Usuario3.depositos(25000)
print("Total depósitos",Usuario3.nombre,":",Usuario3.hacer_deposito)
Usuario3.retiros(10000)
Usuario3.retiros(10000)
Usuario3.retiros(10000)
print("Total retiros",Usuario3.nombre,":",Usuario3.hacer_retiro)
Usuario3.balance()
print("Balance final",Usuario3.nombre,":",Usuario3.mostrar_balance_usuario)"""