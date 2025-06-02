import matplotlib.pyplot as plt
import numpy as np

#creating a list of x and y values
x=[1,2,3,4,5]
y=[1,2,3,4,5]

#plotting them on the graph and showing it
plt.plot(x,y)
plt.show()

plt.plot(x,y,"ro")  #red dot plot
plt.show()

plt.plot(x,y,"g^") #green triangle plot
plt.show()

plt.plot(x,y,"r--") #red straight dash plot
plt.show()
 
plt.plot(x,y,"b--")  #blue straight dash plot
plt.show()

plt.plot(x,y,"b-")   #blue straigh line plot
plt.show()

plt.plot(x,y)
plt.axis([0,10,0,200])
plt.show()

#Key features of the graph

plt.plot(x,y,"r--", label = "Y = X", linewidth = 4)
plt.axis([0,10,0,50])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Graph")
plt.legend()
plt.show()

x=np.arange(0,10,0.2) 
print(x)

y1 = x**2
y2 = x**3

plt.plot(x,y1,"g--",x,y2,"b--")
plt.show()

#Linear Equation Graph

c=1
m=2
x=np.linspace(-5,5,100)
y=m*x+c

plt.plot(x,y,'r--',label = f'y = {m}x + {c}',linewidth = 2)
plt.title("Linear Equation Graph")
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#Bar Chart/Graph

#x cordinate = postion of bar
#y  cordinate  = length of bar

x=[1,3,5,7]
y=[2,6,4,9]

plt.bar(x,y,color = "b")
plt.show()


x1=[1,3,5,7]
y1=[2,4,6,8]

plt.bar(x1,y1,color = 'b')


x2 = [2,4,6,8]
y2 = [1,3,5,7]

plt.bar(x2,y2,color = 'r')
plt.show()

plt.bar(["Male Literacy", "Female Literacy"], [90,95])
plt.show()

plt.bar(['Economy Class', 'Business Class','First Class'],[95,74,51])
plt.show()

x=[]
y=[]

for i in range(5):
    n = int(input("What value do you want x to be "))
    x.append(n)

print(x)

for i in range(5):
    yval = (x[i]*4) + 10
    y.append(yval)

print(y)

plt.plot(x,y,'r--')
plt.title("Custom Equation")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()