import sys 
import random
h = open("data/input/test.txt","w",encoding="utf8")

n, m  = int(sys.argv[1]),int(sys.argv[2])
h.write("{} {}\n".format(n,m))
d = [random.randint(2,6) for i in range(n)]
h.write(" ".join(list(map(str,d)))+"\n")
t = [random.randint(14,20) for i in range(m)]
h.writelines(" ".join(list(map(str,t)))+"\n")
for i in range(n):
    mm = []
    d = random.randint(0,7)
    mm.append(d)
    for i in range(d):
        mm.append(random.randint(0,m-1))

    h.write(" ".join(list(map(str,mm)))+"\n")
kk = int(n/10)
for i in range(n):
    mm = []
    for i in range(n):
        random()
        mm.append(0)

    h.write(" ".join(list(map(str,mm)))+"\n")
h.close()
