width = 80
height = 50

with open("polska.ppm","w") as f:
    f.write("P3\n")
    f.write(f"{width} {height}\n")
    f.write("255\n")
    for y in range(height):
        for x in range(width):
            if y < height / 2:
                f.write(f"{255} {255} {255}\n")
            else:
                f.write(f"{212} {33} {61}\n")