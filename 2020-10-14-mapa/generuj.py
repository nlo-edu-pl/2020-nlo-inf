import random

random.seed( 2021 )

RX = 800
RY = 800
n_sklepy = 3
n_mieszkancy = 10

with open("sklepy.txt","w") as f:
    for i in range( n_sklepy ):
        x = random.randint( 0, RX )
        y = random.randint( 0, RY )

        f.write(f"{x} {y}\n")

with open("mieszkancy.txt", "w") as f:
    for i in range( n_mieszkancy ):
        x = random.randint( 0, RX )
        y = random.randint( 0, RY )

        f.write(f"{x} {y}\n")
