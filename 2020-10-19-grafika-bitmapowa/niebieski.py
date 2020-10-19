width = 256
height = 256

with open("niebieski.ppm","w") as f:
    f.write("P3\n")
    f.write(f"{width} {height}\n")
    f.write("255\n")
    for y in range(height):
        for x in range(width):
            if y % 2 == 0:
                f.write(f"{10} {10} {240}\n")
            else:
                f.write(f"{255} {255} {255}\n")