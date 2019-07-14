import os
import matplotlib.pyplot as plt
import numpy as np


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = '/home/pavel/{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)
    # plt.close()


#############################################################################
########Здесь будут объявляться все переменные, указанные в заданиях#########
#############################################################################

# Задание 1 - картинка с подписью

from PIL import Image

file1 = Image.open('/home/pavel/Загрузки/1.jpg')  # Путь картинки
text_1 = "Cyberbunk 2019"  # Текст заголовка

################Задание 2 - стандартный график Python с заливкой###############
import re

pathtotask2 = "/home/pavel/Загрузки/file_date.txt"  # Переменная, содержащая путь к файлу
var = 13  # Номер выполняемого варианта
file2 = open(pathtotask2, 'r')
i = 0
abc_2 = []  # Массив точек абсцисс 2 задания(нет но да)
val_ar_2 = []  # Значения графика 2 задания
head_text_2 = "Стандартный график"  # Заголовок графика 2 задания
head_font_2 = "Tahoma"  # Шрифт, размер заголовка графика 2 задания
head_size_2 = 14
head_weight_2 = 'bold'
head_style_2 = 'normal'  # Жирность и стиль:'bold', 'normal'

text_font_2 = "Tahoma"  # Шрифт, размер, поворот подписей делений осей координат
text_size_2 = 12
text_deg_turn_2 = 30
text_weight_2 = 'bold'
fill_color_21 = 'grey'  # Заливка, цвет над графиком
# fill_color_22='red'#Заливка под графиком(опционально)
background_color_2 = 'yellow'  # Фон диаграммы Цвет любой;задание цвета -любое

# Обработка данных
for line in file2:  # Извлечение данных
    i += 1
    if (i == 1):
        abc_2 = re.findall(r'\d+', line)

    if (i == var + 1):
        val_ar_2 = re.findall(r"[-+]?\d+\.\d+", line)

# Но это ещё не всё, все значения хранятся в виде строк, их НЕОБХОДИМО преобра-
# вать в численные
abc_2 = np.array(abc_2, int)
val_ar_2 = np.array(val_ar_2, float)
# Опциональная часть для тех, у кого есть значения ниже нуля(Может вылезти
# за границы если будут подряд два значения >0 и <0
# bz_val_ar=[]#Массив для заливания под Ох
#
# for y in val_ar_2:#Создаёт массив только отрицательных значений
#   if(int(y)>0): y = 0
#   bz_val_ar.append(y)
# bz_val_ar = np.array(bz_val_ar,int)
# ax2.fill_between(abc_2,bz_val_ar,0,color = fill_color_22)#Этим методом
# Осуществляется заливка

################Задание 3 - столбчатая диаграмма с аннотацией##############
import re

pathtotask3 = "/home/pavel/Загрузки/fig8.txt"  # Переменная, содержащая путь к файлу
var = 13  # Номер выполняемого варианта
file3 = open(pathtotask3, 'r')
i = 0
abc_30 = 0  # Нулевая точка абсцисс 3 задания
abc_31 = 0  # Конечная точка абсцисс 3 задания
val_ar_3 = []  # Значения графика 3 задания

fill_color_3 = 'black'  # Заливка любая, цвет любой
arrow_color = '#AAAAAA'  # Стрелка Цвет любой;способ задания –HEX
arrow_end_x = 280  # Координаты начала и указателя стрелки
arrow_end_y = 25  #
arrow_head_x = 288.6  #
arrow_head_y = 31  #
arrow_width = 0.5  # Ширина стрелки

text_3 = "Максимум"  # Текст
text_font_3 = "Courier"  # Шрифт текста на поле графика 3 задания
text_size_3 = "16"
text_weight_3 = 'light'  # Жирность и стиль:'light', 'normal'
text_style_3 = 'normal'
text_color_3 = "#abcdeff0"  # Цвет текста
text_x_3 = arrow_end_x - len(text_3)  # Координата х
text_y_3 = arrow_end_y - 2  # Координата y(можно поменять на просто число)

background_color_3 = 'brown'  # Фон диаграммы Цвет любой;задание цвета -любое
for line in file3:
    i += 1
    if (i == 2 * var - 1):
        values = re.findall(r'\d+', line)
        abc_30 = values[0]
        abc_31 = values[1]
    if (i == 2 * var):
        val_ar_3 = re.findall(r'\d+', line)
abc_3 = np.arange(int(abc_30), int(abc_31) + 1, 1)
val_ar_3 = np.array(val_ar_3, int)
######################Задание 4 - график функций с легендой####################
import math

abc_4 = np.arange(-1.0 * math.pi, math.pi / 2, math.pi / 120)  # Создание массива координат х
val_ar_4_1 = []  # Массив значений y1
y2_k = -0.12  # Коэффициент функции y2
polynom_sq = [-1.8, -1, -0.13, -0.5, 1.9]  # Корни полинома
val_ar_4_2 = []  # Массив значений y2
y1_color = 'cyan'  # Цвет первого графика
y2_color = 'magenta'  # Цвет второго графика
legend_font = "Times New Roman"  # Данные легенды:шрифт, цвет, размер, жирность, стиль и цвет
legend_size = 16
legend_weight = 'light'
legend_style = 'normal'
legend_color = 'green'
legend_turn_ox = 15  # Угол поворота значений Ох
legend_text_1 = "sin(4x)-cos(6x)^2"  # Текст легенды 1 и 2 графика
legend_text_2 = "Полином с k = 0.12"
# Обработка
legend_props = {  # Без него не передать инфу о шрифте в легенду
    'family': legend_font,
    'size': legend_size,
    'weight': legend_weight,
    'style': legend_style,
}
for x in abc_4:
    val_ar_4_1.append(math.sin(x * 4.0) - math.cos(x * 6.0) ** 2)  # Задание массива значений 1 функции
val_ar_4_1 = np.array(val_ar_4_1, float)

k_array = np.poly(polynom_sq)  # Массив коэфициентов уравнения y2
for i in range(0, len(k_array)):  # преобразуем на общий коэфициент
    k_array[i] = k_array[i] * y2_k
for x in abc_4:
    sum = 0
    for k in range(0, len(k_array)):
        sum += k_array[k] * (x ** (len(k_array) - k - 1))

    val_ar_4_2.append(sum)
val_ar_4_2 = np.array(val_ar_4_2, float)

####################Задание 5 -Диаграммы рассеяния#############################
import scipy as sc

pareto_alpha = 1  # Коэффициент для распр. Парето
norm_myu = 3.0  # Коэффициенты для нормального расп.
norm_sigma = 2.0
gamma_shape = 1.0  # Коэффициенты для гамма расп.
gamma_scale = 1.7
ravn_min = 0  # Коэффициенты для равномерного расп.
ravn_max = 3
pareto_color = 'red'  # Цвета графиков распределений
norm_color = [0, 1, 0]
gamma_color = 'orange'
ravn_color = '#0080FF'
pareto_dotsize = 10;  # размер точек распределений
norm_dotsize = 3;
gamma_dotsize = 2;
ravn_dotsize = 1;
abc_5_1 = np.arange(0.001, 1, 1 / 300)  # Задаём абсциссу для 1 функции
abc_5_2 = np.arange(1.001, 2, 1 / 300)
abc_5_3 = np.arange(2.001, 3, 1 / 300)
# Поиск значений
# Распределение Парето
# val_ar_5_pareto = np.random.pareto(abc_5)
# for i in range(0,len(val_ar_5_pareto)):
#   val_ar_5_pareto[i]*=pareto_alpha
# Задаём нормальное распределение
val_ar_5_normal = np.random.normal(norm_myu, norm_sigma, 300)
# Задаём гамма распределение
val_ar_5_gamma = np.random.gamma(gamma_shape, gamma_scale, 300)
# Задаём равномерное распределение
val_ar_5_ravn = np.random.uniform(ravn_min, ravn_max, 300)
# Задание 6 - График фигур Лиссажу с заливкой
import math

ampl_a = 6  # Амплитуды А и В
ampl_b = 15
freq_a = 7.2  # Частоты a и b
freq_b = 6
lis_sigma = math.pi / 4  # Cдвиг фаз
lis_color = "#0000FF"  # Цвет заливки
lis_transparency = 0.2  # Прозрачность(от 0 до 1
lis_netline_color = '#FF0000'  # Цвет линий сетки

# Обработка
abc_6 = []
val_ar_6 = []
for i in range(0, 1001):
    abc_6.append(ampl_a * math.sin(math.pi * i / 500 * freq_a + lis_sigma))
    val_ar_6.append(ampl_b * math.sin(math.pi * i / 500 * freq_b))
abc_6 = np.array(abc_6, float)
val_ar_6 = np.array(val_ar_6, float)
#############################################################################
#####################Конец объявления переменных#############################
#############################################################################

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.font_manager as fmg

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
ax2.plot(abc_2, val_ar_2)  # Ставим точки графика по знач. двух массивов
plt.sca(ax2)  # Переключаемся на оси 2 графика
ax2.grid(True)  # Включаем решетку графика
ax2.set_xlabel('Время', fontsize=text_size_2, fontname=text_font_2)  # Подпись оси х
ax2.set_ylabel('Температура', fontsize=text_size_2, fontname=text_font_2)  # оси y
ax2.set_title(head_text_2, fontsize=head_size_2, fontname=head_font_2,  # Заголовок
              fontstyle=head_style_2, fontweight=head_weight_2)
ax2.set_facecolor(background_color_2)
plt.xticks(rotation=text_deg_turn_2)  # Поворачиваем значения оси х
plt.yticks(rotation=text_deg_turn_2)  # Поворачиваем значения оси y

ax2.fill_between(abc_2, 0, val_ar_2, color=fill_color_21)  # Заливка над Ох
ax2.set_title("Стандартный график с заливкой")
# Конец задания 2

# Начало задания 3
ax3.bar(abc_3, val_ar_3, color=fill_color_3)  # Создание столбцов диаграммы
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
p1, = ax4.plot(abc_4, val_ar_4_1, color=y1_color)  # Рисуем графики по массивам
p2, = ax4.plot(abc_4, val_ar_4_2, color=y2_color)

l = ax4.legend([p1, p2], [legend_text_1, legend_text_2], prop=legend_props, loc=0)  # Создаём легенду
for text in l.get_texts():  # ЗАДАЁМ ЦВЕТ ТАК ПОТОМУ ЧТО ПО НОРМАЛЬНОМУ НЕЛЬЗЯ
    text.set_color(legend_color)
plt.sca(ax4)  # Переключаемся на 4 подграфик для поворота осей

plt.xticks(rotation=legend_turn_ox)  # Поворачиваем оси
ax4.grid(True)  # Включаем решётку
ax4.set_title("График с легендой")
# Конец 4 задания

# Начало задания 5
# ax5.plot(abc_5(Заменить на нужное),val_ar_5_pareto, '.',linewidth = pareto_dotsize, color = pareto_color)#Рисуем распределение Парето
ax5.scatter(abc_5_1, val_ar_5_normal, norm_dotsize, norm_color)  # Рисуем нормальное распределение
ax5.scatter(abc_5_2, val_ar_5_gamma, gamma_dotsize,  # Рисуем гамма распределение
            color=gamma_color)
ax5.scatter(abc_5_3, val_ar_5_ravn, ravn_dotsize, ravn_color)  # Рисуем равномерное распределение
ax5.grid(True)
ax5.set_facecolor("#000000")  # Задаём цвет фона
ax5.set_title("Диаграмма рассеяния")
# Конец задания 5

# Начало задания 6
ax6.plot(abc_6, val_ar_6)  # Построение графика
ax6.fill_between(abc_6, val_ar_6, color=lis_color, alpha=lis_transparency)  # Заливка фигуры
ax6.grid(color=lis_netline_color)
ax6.set_title("Фигуры Лиссажу")
# Конец задания 6
plt.show()
