#Данные "Покер"
*Источник данных [Poker Hand](http://archive.ics.uci.edu/ml/datasets/Poker+Hand)*

###Описание формата
Данные разделены на две части Тренировочная и Тестовая

+ **train_samples.csv**  Тренировочные примеры (25,010)
+ **train_answers.csv**  Ответы к тренировочным примерам (25,010)
+ **test_samples.csv**   Тестовые примеры (1,000,000)
+ **test_answers.csv**   Ответы к тестовым примерам (1,000,000)

#### Примеры

Каждый пример - описание руки в покере из пяти карт (85 атрибутов). Каждая карта описывается бинарным вектором из 17 атрибутов:

* Первые 4 значения - цвет карты *(isHearts, isSpades, isDiamonds, isClubs)*
* Следующие 13 значений - ранг карты *(isAce, is2, is3, ... , isQueen, isKing)*

#### Ответы
Каждый ответ - тип комбинации в покере, который описывается соответственным примером. Каждый ответ описывается бинарным вектором из 10 атрибутов:

* *(isNothing, isOnePair, isTwoPairs, isThreeOfAKind, isStraight, isFlush, isFullHouse, isFourOfAKind, isStraightFlush, isRoyalFlush)*

#### Расшифорвка

1. Nothing in hand; not a recognized poker hand 
2. One pair; one pair of equal ranks within five cards
3. Two pairs; two pairs of equal ranks within five cards
4. Three of a kind; three equal ranks within five cards
5. Straight; five cards, sequentially ranked with no gaps
6. Flush; five cards with the same suit
7. Full house; pair + different rank three of a kind
8. Four of a kind; four equal ranks within five cards
9. Straight flush; straight + flush
10. Royal flush; {Ace, King, Queen, Jack, Ten} + flush


