#Данные "Покер"
*Источник данных [Titanic](http://www.kaggle.com/c/titanic-gettingStarted/data)*

###Описание формата
Данные разделены на две части Тренировочная и Тестовая

+ **train_samples.csv**  Тренировочные примеры (1526)
+ **train_answers.csv**  Ответы к тренировочным примерам (1526)
+ **test_samples.csv**   Тестовые примеры (673)
+ **test_answers.csv**   Ответы к тестовым примерам (673)

#### Примеры

Каждый пример - описание пассажира (6 атрибутов). Каждая человек описывается бинарным вектором из 6 атрибутов:

* Первые 4 значения - класс пассажира *(1 class, 2 class, 3 class, Crew)*
* Пол *(male, female)*
* Возраст *(child, adult)*

#### Ответы
Каждый ответ - булево значение - выжил или нет