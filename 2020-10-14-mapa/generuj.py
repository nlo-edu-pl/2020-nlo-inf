import random

random.seed( 2021 )

RX = 800
RY = 800
n_sklepy = 30
n_mieszkancy = 1000

with open("sklepy.txt","w") as f:
    for i in range( n_sklepy ):
        x = random.randint( 0, RX - 1 )
        y = random.randint( 0, RY - 1 )

        f.write(f"{x} {y}\n")

with open("mieszkancy.txt", "w") as f:
    for i in range( n_mieszkancy ):
        x = random.randint( 0, RX - 1 )
        y = random.randint( 0, RY - 1 )

        f.write(f"{x} {y}\n")
