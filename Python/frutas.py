import random
import time
n = []
random.randint()


while True:
    random.shuffle(n)
    print(f"{n} Aoba \n")
    if n == [1,2,3,5,6]:
        print("Olá mundo \n")
        break
    else:
        print("Olá marte")
        print(n)
    time.sleep(0.5)