# Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x 
# значение функции отрицательно.

import matplotlib.pyplot as plt
import sympy as sp



x = sp.Symbol('x')
y = 5*x**2+10*x-30

plt.plot(y)
plt.show()