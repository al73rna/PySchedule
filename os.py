__author__ = 'mohammadreza barazesh 91521059'

import math
import matplotlib
tasks = []
finishedTasks = []

class task():
    def __init__(self,et,at):
        self.execTime = et
        self.arrivalTime = at
        self.exitTime = None
        self.waitTime = 0


class FIFO():
    def __init__(self):
        self.l = []
    def pop(self):
        return self.l.pop(0)
    def push(self,x):
        self.l.append(x)

class LIFO():
    def __init__(self):
        self.l = []
    def pop(self):
        return self.l.pop()
    def push(self,x):
        self.l.append(x)

class SJF():
    def __init__(self):
        self.l = []
    def pop(self):
        current = 0
        sj = 1000
        for i in range(len(self.l)):
            if self.l[i].execTime < sj :
                sj = self.l[i].execTime
                current = i
        return self.l.pop(current)
    def push(self,x):
        self.l.append(x)

class RR():
    def __init__(self):
        self.l = []
        self.rt = 20
    def pop(self):
        pass
    def push(self,x):
        self.l.append(x)

# plz fill the Qs

print("Choose the method :")
print("1-FIFO")
print("2-LIFO")
print("3-SJF")
print("4-RR")
m = input("enter number ...")

t = 0

if int(m) == 1 :
    tsk = FIFO()
    while(len(tsk.l)>0) :
        if tsk.l[0].execTime > 0 :
            tsk.l[0].execTime -= 1
        else:
            p = tsk.pop()
            p.exitTime = t
            finishedTasks.append(p)
        for i in tsk.l :
            i.waitTime += 1
        t += 1
if int(m) == 2 :
    tsk = LIFO()
    while(len(tsk.l)>0) :
        if tsk.l[-1].execTime > 0 :
            tsk.l[-1].execTime -= 1
        else:
            p = tsk.pop()
            p.exitTime = t
            finishedTasks.append(p)
        for i in tsk.l :
            i.waitTime += 1
        t += 1
if int(m) == 3 :
    tsk = SJF()
    while(len(tsk.l)>0) :
        current = 0
        sj = 1000
        for i in range(len(tsk.l)):
            if tsk.l[i].execTime < sj :
                sj = tsk.l[i].execTime
                current = i
        top =  current
        if tsk.l[top].execTime > 0 :
            tsk.l[top].execTime -= 1
        else:
            p = tsk.pop()
            p.exitTime = t
            finishedTasks.append(p)
        for i in tsk.l :
            i.waitTime += 1
        t += 1
if int(m) == 4 :
    rt = int(input("Time ?"))
    tsk = RR()
    while(len(tsk.l)>0) :
        it = math.floor( t/rt )
        if tsk.l[it].execTime > 0 :
            tsk.l[it].execTime -= 1
        else:
            p = tsk.l.pop(it)
            p.exitTime = t
            finishedTasks.append(p)
        for i in tsk.l :
            i.waitTime += 1
        t += 1
T_Exec = 0
T_W = 0
T_TT =0
for t in finishedTasks :
    T_Exec += i.execTime
    T_W += i.waitTime
    T_TT += i.exitTime - i.arrivalTime
    print(i.execTime)
    print(i.waitTime)
    print(i.exitTime - i.arrivalTime)
