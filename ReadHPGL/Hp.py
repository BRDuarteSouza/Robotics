# Hp.py
# Read HPGL file and convert into pulses for a step motor
# Author:Bruno Duarte <brduarte95@gmail.com>

import math
import matplotlib.pyplot as plt



def step(D,theta,xo,yo):
    abs = []
    ord = []
    for p in range(0,D):
        x = math.floor(p*math.cos(theta))
        abs.append((xo+x))
        y = math.floor(p*math.sin(theta))
        ord.append((yo+y))
        # print("pontos:({},{})".format(x,y))
    print("x:{} \n  y:{}".format(abs,ord))
    plt.plot(abs,ord, "ro")
    plt.show()

def main():
    # f = open("exp.plt","r")
    # arq = f.readlines()
    # # for x in range(0,len(arq)):
    # cmd = arq[0]
    # if(cmd[1] == "U"):
    #     print("action:{}  pontos:{}".format(act,pos))
    text = input("type coordinates: \n")
    p1,p2 = text.split(" ")
    xo,yo = p1.split(",")
    x1,y1 = p2.split(",")
    D = math.floor(math.sqrt(math.pow(int(x1)-int(xo),2) + math.pow(int(y1)-int(yo),2)))
    theta = math.atan((int(y1)-int(yo))/(int(x1)-int(xo)))
    # theta = math  .degrees(theta)

    step(D,theta,int(xo),int(yo))

    print("minha reta: {} {}º".format(D,theta))







if __name__ == '__main__':
    main()
