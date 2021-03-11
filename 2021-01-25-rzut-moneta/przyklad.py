# https://logia.oeiizk.waw.pl/#!/bankzadan

from turtle import *

def prostokat(a, b, kolor):
    color('black', kolor)
    begin_fill()
    for i in range(2):
        fd(a)
        lt(90)
        fd(b)
        lt(90)
    end_fill()

prostokat(300, 250, 'yellow')

done()