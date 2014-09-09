#!/usr/bin/env python
import scipy as sp
import matplotlib.pyplot as plt

def error(f,x,y):
  return sp.sum((f(x)-y)**2)


#loading data
#____________________
data = sp.genfromtxt("/Users/avinashkulkarni/data.tsv",delimiter = "\t")
x = data[:,0]
y = data[:,1]


#polynomial fitting
#____________________
fp1,residuals,rank,sv,rcond = sp.polyfit(x,y,1,full=True)
f1 = sp.poly1d(fp1)
print(error(f1,x,y))
#____________________
f2p = sp.polyfit(x,y,2)
f2 = sp.poly1d(f2p)
print(error(f2,x,y))
#____________________
f3p = sp.polyfit(x,y,3)
f3 = sp.poly1d(f3p)
print(error(f3,x,y))

#plotting
#____________________
plt.scatter(x,y)
plt.title("Quadratic Plot")
plt.xlabel("time")
plt.ylabel("Hits")
#plt.xticks
fx=sp.linspace(0,x[-1],30)
plt.plot(fx,f1(fx),linewidth=1)
plt.plot(fx,f2(fx),linewidth=1)
plt.plot(fx,f3(fx),linewidth=1)
plt.autoscale(tight=True)
plt.grid()
plt.show()


#========================
