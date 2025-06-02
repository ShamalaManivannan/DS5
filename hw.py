import matplotlib.pyplot as plt
import numpy as np

print("Choose the type of equation to plot:")
print("1.Linear")
print("2.Quadratic")
print("3.Cubic")

choice = input("Enter your choice 1,2,3: ")

x = np.linspace(0, 50, 1000)

if choice == '1':
    m = float(input("Enter the value of m: "))
    c = float(input("Enter the value of c: "))
    y = m*x+c
    plt.plot(x, y, 'r--', label=f'y = {m}x + {c}', linewidth=2)
    plt.title("Linear Equation Graph")
    
elif choice == '2':
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    y = a*x**2+b*x+c
    plt.plot(x, y, 'g--', label=f'y = {a}x² + {b}x + {c}', linewidth=2)
    plt.title("Quadratic Equation Graph")
    
elif choice == '3':
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    d = float(input("Enter the value of d: "))
    y = a * x**3 + b * x**2 + c * x + d
    plt.plot(x, y, 'b--', label=f'y = {a}x³ + {b}x² + {c}x + {d}', linewidth=2)
    plt.title("Cubic Equation Graph")

else:
    print("Invalid choice!")


plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.axis([0,50,0,10000])
plt.show()