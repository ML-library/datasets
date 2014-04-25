#Данные "Adult"
*Источник данных [Adult](http://archive.ics.uci.edu/ml/datasets/Adult)*

###Описание формата
Данные разделены на две части Тренировочная и Тестовая

+ **train_samples.csv**  Тренировочные примеры (32561)
+ **train_answers.csv**  Ответы к тренировочным примерам (32561)
+ **test_samples.csv**   Тестовые примеры (16281)
+ **test_answers.csv**   Ответы к тестовым примерам (16281)

#### Примеры

Каждый пример - описание человека (123 бинарных атрибута):

age: <26, <33, <41, <50, >=50.
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
fnlwgt: wgt<106648, wgt<158662, wgt<196338, wgt<259873, wgt>=259873.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
education-num: eduVal<9, eduVal<10, eduVal<11, eduVal<13, eduVal>=13.
marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
capital-gain: gain<1, gain>=1.
capital-loss: loss<1, loss>=1.
hours-per-week: hours<35, hours<40, hours<41, hours<48, hours>=48.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.


#### Ответы
Каждый ответ - булево значение - зарабатывает ли человек 50K в год.
