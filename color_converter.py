# Программа для конвертации цветов

# Ввод цвета от пользователя в формате RGB
red = int(input("Введите значение красного цвета (0-255): "))
green = int(input("Введите значение зеленого цвета (0-255): "))
blue = int(input("Введите значение синего цвета (0-255): "))

# Конвертация RGB в HSV
h = 0.0
s = 0.0
v = 0.0

r = red / 255.0
g = green / 255.0
b = blue / 255.0

max_value = max(r, g, b)
min_value = min(r, g, b)
diff = max_value - min_value

if max_value == min_value:
    h = 0
elif max_value == r:
    h = (60 * ((g - b) / diff) + 360) % 360
elif max_value == g:
    h = (60 * ((b - r) / diff) + 120) % 360
elif max_value == b:
    h = (60 * ((r - g) / diff) + 240) % 360

if max_value == 0:
    s = 0
else:
    s = (diff / max_value) * 100

v = max_value * 100

# Конвертация RGB в HEX
hex_value =
