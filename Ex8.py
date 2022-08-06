import math
x1 = int(input("Input first cordinate of P: "))
y1 = int(input("Input second cordinate of P: "))
x2 = int(input("Input first cordinate of Q: "))
y2 = int(input("Input second cordinate of Q: "))

dist_ = math.dist([x1,y1], [x2, y2])
print("Distance between two coordinates : ", round(dist_,2))