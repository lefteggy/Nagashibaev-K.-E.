# TODO решите задачу
def task() -> float:
    x = 0
    sch = 0
    sum = 0
    c1 = 0
    c2 = 0
    f = open("input.json", "r")
    x = f.readlines()
    for i in range(len(x)):
        if x[i].find("score") != -1:
            c1 = float(x[i][((x[i].find("score")) + 8):len(x[i]) - 2])
        elif (x[i].find("weight")) != -1:
            c2 = float(x[i][((x[i].find("weight")) + 9):len(x[i]) - 1])
        if(c1 != 0) and (c2 != 0):
            sum += c1 * c2
            c1, c2 = 0, 0
    f.close()
    return round(sum, 3)

print(task())

