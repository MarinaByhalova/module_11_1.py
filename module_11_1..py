import numpy as np

# Создание массива из списка. Сложение массивов.
a = np.array([1, 3, 6, 9, 11])
b = np.array([2, 4, 5, 12, 16])
print(a)
print(b)
print(a + b)

# Создание двумерного массива из списка списков.Умножение массивов.
a = np.array([[5, 8, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[4, 7, 6], [1, 2, 3], [11, 2, 5]])
print(a)
print(b)
print(a * b)

# Создание массива из единиц. Умножение массива на число.
a = np.ones((2, 2))
print(a)
print(a * 3)

import pandas as pd

students = {'Студент': ['Иванов', 'Петров', 'Сидоров', 'Кузнецов'],
        'Год рождения': [1987, 1986, 1979, 1989]}
# Превращение  словаря в DataFrame, используя стандартный метод библиотеки.
df = pd.DataFrame(students)
print(df)

# создание Series из списка
data1 = [5, 10, 20, 30, 40]
series1 = pd.Series(data1)
print(series1)


from PIL import Image
#Работа с изображениями
image = Image.open('3086.jpg')
image = Image.open('3086.jpg')
image.save('3086_formatted.png')
image = Image.open('3086.jpg')
image.thumbnail((200, 200))
image.save('3086_thumbnail.jpg')
image = Image.open('3086.jpg')
grayscale_image = image.convert('L')
grayscale_image.save('3086_grayscale.jpg')


