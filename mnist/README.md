#Данные "Рукописные цифры"
*Источник данных [MNIST](http://yann.lecun.com/exdb/mnist/)*

###Описание формата
Данные разделены на две части Тренировочная и Тестовая

+ **train_samples.csv**  Тренировочные примеры (60,000)
+ **train_answers.csv**  Ответы к тренировочным примерам (60,000)
+ **test_samples.csv**   Тестовые примеры (10,000)
+ **test_answers.csv**   Ответы к тестовым примерам (10,000)

#### Примеры

Каждый пример - картинка 28х28 пикселей (784 атрибута). Каждая цифра описывается вектором из значений яркости пикселей от 0 до 255.
0 означает фон (белый цвет), 255 означает передний план (черный цвет). Пиксели выписаны построчно.

#### Ответы
Каждый ответ - цифра, изображенная на картинке.