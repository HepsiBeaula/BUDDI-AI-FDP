import numpy as np
import matplotlib.pyplot as plt
txt="The plot that shows the Lagrange's polynomial"

def lagrange(X, Y, xi, n):
    res=0.0
    for i in range(n):
        t=Y[i]
        for j in range(n):
            if(j!=i):
                t=t*(xi-X[j])/(X[i]-X[j])
        res+=t
    return res

X=[-3,-2,-1,0,1,2,3]
Y=[7,2,0,0,0,2,7]
n=len(X)
YCap=[lagrange(X,Y,X[i],n) for i in range(n)]
print(YCap)

plt.title("Applying Lagrange's polynomial ")
plt.scatter(X,Y, marker="x", label="Original data points")
plt.plot(X,YCap, color="blue", label="Lagrange's polynomial ")
plt.figtext(0.8, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=8)
plt.legend()
plt.show()
