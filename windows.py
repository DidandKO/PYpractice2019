from PIL import Image
import numpy as np

# Ввод данных

# Задание 1 - картинка с подписью

file1 = Image.open('sun.jpg')  # Путь картинки
text_1 = "Sun"  # Текст заголовка

# Задание 2 - стандартный график Python с заливкой
var = 7  # Номер выполняемого варианта
i = 0
x_2 = np.arange(1, 28, 1)   # Массив точек абсцисс 2 задания
y_2 = [2.9,  -1.5,  -3.6,   0.7,   5.1,   8.5,
       6.5,  4.7,   6.8,   6.2,   1.9,  -3.5,
       -1.3,   2.4,   3.5,   4.4,   4.1,   5.6,
       -1.8,   1.1,   0.2,   2.9,   1.8,   1.8,
       3.8,   7.2,   7.9]  # Значения графика 2 задания
head_text_2 = "Стандартный график"  # Заголовок графика 2 задания
head_font_2 = "Times New Roman"  # Шрифт, размер заголовка графика 2 задания
head_size_2 = 12
head_weight_2 = 'bold'
head_style_2 = 'oblique'  # Жирность и стиль:'bold', 'oblique'

text_font_2 = "Tahoma"  # Шрифт, размер, поворот подписей делений осей координат
text_size_2 = 12
text_deg_turn_2 = 30
text_weight_2 = 'bold'
fill_color_2 = 'grey'  # Заливка, цвет над графиком #808080-HEX код
background_color_2 = 'yellow'  # Фон диаграммы Цвет любой;задание цвета -любое #FFFF00 - HEX код

# Задание 3 - столбчатая диаграмма с аннотацией

i = 0
x_3 = np.arange(616, 667, 1)  # Нулевая точка абсцисс 3 задания
print(x_3)
# abc_31 = 0  # Конечная точка абсцисс 3 задания
y_3 = [2, 4, 5, 16, 0, 0, 17, 3, 0, 0, 4, 6, 2, 0, 8, 0, 0, 6, 2,
       4, 5, 11, 0, 0, 12, 2, 4, 0, 0, 0, 0, 0, 0, 4, 6, 2, 0, 0,
       1, 1, 11, 0, 0, 0, 2, 0, 3, 13, 0, 0, 2]  # Значения графика 3 задания
print(y_3)

fill_color_3 = 'black'  # Заливка любая, цвет любой
arrow_color = '#AAAAAA'  # Стрелка Цвет любой;способ задания –HEX
arrow_end_x = 280  # Координаты начала и указателя стрелки
arrow_end_y = 25  #
arrow_head_x = 288.6  #
arrow_head_y = 31  #
arrow_width = 0.5  # Ширина стрелки

text_3 = "Максимум"  # Текст
text_font_3 = "Tahoma"  # Шрифт текста на поле графика 3 задания
text_size_3 = "16"
text_weight_3 = 'light'  # Жирность и стиль:'light', 'normal'
text_style_3 = 'normal'
text_color_3 = "#abcdeff0"  # Цвет текста
text_x_3 = arrow_end_x - len(text_3)  # Координата х
text_y_3 = arrow_end_y - 2  # Координата y(можно поменять на просто число)

background_color_3 = 'brown'  # Фон диаграммы Цвет любой;задание цвета -любое

# Задание 4 - график функций с легендой

import math

x_4 = np.arange(-1.0 * math.pi, math.pi / 2, math.pi / 120)  # Создание массива координат х
y4_1 = []  # Массив значений y1
ky4 = 0.3  # Коэффициент функции y2
polynom_sq = [-1.8, -0.3, 0, 35, 1.9]  # Корни полинома
y4_2 = []  # Массив значений y2
y1_color = 'cyan'  # Цвет первого графика
y2_color = 'magenta'  # Цвет второго графика
legend_font = "Times New Roman"  # Данные легенды:шрифт, цвет, размер, жирность, стиль и цвет
legend_size = 15
legend_weight = 'light'
legend_style = 'oblique'
legend_color = 'green'
legend_turn_ox = 45  # Угол поворота значений Ох
legend_text_1 = "sin(x)+sin(4x)"  # Текст легенды 1 и 2 графика
legend_text_2 = "Полином с k = 0.3"
# Обработка
legend_props = {
    # Без него не передать инфу о шрифте в легенду
    'family': legend_font,
    'size': legend_size,
    'weight': legend_weight,
    'style': legend_style,
}
for x in x_4:
    y4_1.append(math.sin(x) - math.cos(x * 4.0))  # Задание массива значений 1 функции
y4_1 = np.array(y4_1, float)

k_array = np.poly(polynom_sq)  # Массив коэфициентов уравнения y2
for i in range(0, len(k_array)):  # преобразуем на общий коэфициент
    k_array[i] = k_array[i] * ky4
for x in x_4:
    sum = 0
    for k in range(0, len(k_array)):
        sum += k_array[k] * (x ** (len(k_array) - k - 1))

    y4_2.append(sum)
y4_2 = np.array(y4_2, float)

# Задание 5 -Диаграммы рассеяния

pareto_alpha = 2.2  # Коэффициент для распр. Парето
norm_myu = 4.0  # Коэффициенты для нормального расп.
norm_sigma = 2.0
gamma_shape = 2.8  # Коэффициенты для гамма расп.
gamma_scale = 2.0
ravn_min = 0  # Коэффициенты для равномерного расп.
ravn_max = 3
pareto_color = [255, 255, 0]  # Цвета графиков распределений
norm_color = 'white'
gamma_color = '#00FF00'
ravn_color = '#FFFFFF'
pareto_dotsize = 10;  # размер точек распределений
norm_dotsize = 2;
gamma_dotsize = 1;
ravn_dotsize = 2;
x_5_1 = np.arange(0.001, 1, 1 / 300)  # Задаём абсциссу для 1 функции
x_5_2 = np.arange(1.001, 2, 1 / 300)
x_5_3 = np.arange(2.001, 3, 1 / 300)
# Поиск значений
# Задаём нормальное распределение
res_normal = np.random.normal(norm_myu, norm_sigma, 300)
# Задаём гамма распределение
res_gamma = np.random.gamma(gamma_shape, gamma_scale, 300)
# Задаём равномерное распределение
res_ravn = np.random.uniform(ravn_min, ravn_max, 300)

# Задание 6 - График фигур Лиссажу с заливкой
import math

ampl_a = 12  # Амплитуды А и В
ampl_b = 15
freq_a = 4  # Частоты a и b
freq_b = 8.4
lis_sigma = math.pi / 2  # Cдвиг фаз
lis_color = "#00FFFF"  # Цвет заливки
lis_transparency = 0.2  # Прозрачность(от 0 до 1)
lis_netline_color = '#0000FF'  # Цвет линий сетки

# Обработка
x_6 = []
y_6 = []
for i in range(0, 1001):
    x_6.append(ampl_a * math.sin(math.pi * i / 500 * freq_a + lis_sigma))
    y_6.append(ampl_b * math.sin(math.pi * i / 500 * freq_b))
x_6 = np.array(x_6, float)
y_6 = np.array(y_6, float)

#Конец ввода данных

import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(16, 12)
egrid = (2, 3)  # Создаём шесть областей для графиков 2х3
ax1 = plt.subplot2grid(egrid, (0, 0))
ax2 = plt.subplot2grid(egrid, (0, 1))
ax3 = plt.subplot2grid(egrid, (0, 2))
ax4 = plt.subplot2grid(egrid, (1, 0))
ax5 = plt.subplot2grid(egrid, (1, 1))
ax6 = plt.subplot2grid(egrid, (1, 2))

# Начало выполнения задания 1
ax1.imshow(file1)  # Вставка файла в график
ax1.set_title(text_1)  # Вставка заголовка
ax1.axis('off')  # Вырубаем оси
# Конец выполнения задания 1

# Начало выполнения задания 2
ax2.plot(x_2, y_2)  # Ставим точки графика по знач. двух массивов
plt.sca(ax2)  # Переключаемся на оси 2 графика
ax2.grid(True)  # Включаем решетку графика
ax2.set_xlabel('Время', fontsize=text_size_2, fontname=text_font_2)  # Подпись оси х
ax2.set_ylabel('Температура', fontsize=text_size_2, fontname=text_font_2)  # оси y
ax2.set_title(head_text_2, fontsize=head_size_2, fontname=head_font_2,  # Заголовок
              fontstyle=head_style_2, fontweight=head_weight_2)
ax2.set_facecolor(background_color_2)
plt.xticks(rotation=text_deg_turn_2)  # Поворачиваем значения оси х
plt.yticks(rotation=text_deg_turn_2)  # Поворачиваем значения оси y

ax2.fill_between(x_2, 0, y_2, color=fill_color_2)  # Заливка над Ох
ax2.set_title("Стандартный график с заливкой")
# Конец задания 2

# Начало задания 3
ax3.bar(x_3, y_3, color=fill_color_3)  # Создание столбцов диаграммы
ax3.grid(which='major', axis='both')  # Создание сетки на диаграмме
ax3.arrow(arrow_end_x, arrow_end_y, arrow_head_x - arrow_end_x,
          arrow_head_y - arrow_end_y, color=arrow_color, width=arrow_width,
          length_includes_head=True)  # Создание стрелки
ax3.text(text_x_3, text_y_3, text_3, fontname=text_font_3,  # Пишем текст
         fontsize=text_size_3, fontstyle=text_style_3,
         fontweight=text_weight_3, color=text_color_3)  #
ax3.set_facecolor(background_color_3)  # Задаём цвет фона
ax3.set_title("Диаграмма с аннотацией")
# Конец задания 3

# Начало задания 4
p1, = ax4.plot(x_4, y4_1, color=y1_color)  # Рисуем графики по массивам
p2, = ax4.plot(x_4, y4_2, color=y2_color)

_legend_ = ax4.legend([p1, p2], [legend_text_1, legend_text_2], prop=legend_props, loc=0)  # Создаём легенду
for text in _legend_.get_texts():  # Задаем цвет
    text.set_color(legend_color)
plt.sca(ax4)  # Переключаемся на 4 подграфик для поворота осей

plt.xticks(rotation=legend_turn_ox)  # Поворачиваем оси
ax4.grid(True)  # Включаем решётку
ax4.set_title("График с легендой")
# Конец 4 задания

# Начало задания 5
ax5.scatter(x_5_1, res_normal, norm_dotsize, norm_color)  # Рисуем нормальное распределение
ax5.scatter(x_5_2, res_gamma, gamma_dotsize,  # Рисуем гамма распределение
            color=gamma_color)
ax5.scatter(x_5_3, res_ravn, ravn_dotsize, ravn_color)  # Рисуем равномерное распределение
ax5.grid(True)
ax5.set_facecolor("#000000")  # Задаём цвет фона
ax5.set_title("Диаграмма рассеяния")
# Конец задания 5

# Начало задания 6
ax6.plot(x_6, y_6)  # Построение графика
ax6.fill_between(x_6, y_6, color=lis_color, alpha=lis_transparency)  # Заливка фигуры
ax6.grid(color=lis_netline_color)
ax6.set_title("Фигуры Лиссажу")
# Конец задания 6
# Показ
plt.show()
# Конец работы
