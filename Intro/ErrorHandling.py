

x = 47
y = 0

try:
    print(x / y)
except ZeroDivisionError as e:
    print(e)
else:
    print("Erro não tratado")
finally:
    print("Finally")