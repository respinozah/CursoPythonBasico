import time

num = int(input("Digite la tabla de multiplicar a usar: "))

for i in range(5,11):
    print(f"{i} por {num} = {i * num}")
    time.sleep(1)