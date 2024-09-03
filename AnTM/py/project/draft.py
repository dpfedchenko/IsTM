import matplotlib.pyplot as plt
import numpy as np

# Создаем данные для графиков
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Создаем первое окно с графиком синуса
plt.figure(1)  # Создаем первое окно
plt.plot(x, y1, color='blue')
plt.title('График синуса')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Создаем второе окно с графиком косинуса
plt.figure(2)  # Создаем второе окно
plt.plot(x, y2, color='red')
plt.title('График косинуса')
plt.xlabel('x')
plt.ylabel('cos(x)')

# Показываем оба графика
plt.show()