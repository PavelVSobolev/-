filename1 = input("Введите путь к файлу 1: ")
filename2 = input("Введите путь к файлу 2: ")
file_in1 = open(filename1, "r")
char = []
for line in file_in1:
    char.append(line.rstrip("\n"))
file_in1.close()
x, y = map(int, char[0].split())
r = float(char[1])
file_in2 = open(filename2, "r")
coord = []
for line in file_in2:
    c0 = line.rstrip("\n")
    c = c0.split()
    coord.append(c)
file_in2.close()
for xy in coord:
    x0 = float(xy[0])
    y0 = float(xy[1])
    d = ((x - x0)**2 + (y - y0)**2)**0.5
    if d > r:
        print(2)
    elif d == r:
        print(0)
    else:
        print(1)

