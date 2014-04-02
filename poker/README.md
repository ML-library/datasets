Источник данных http://archive.ics.uci.edu/ml/datasets/Poker+Hand
Данные разделены на две части Тренировочная и Тестовая

train_samples.csv  Тренировочные примеры (25,010)
train_answers.csv  Ответы к тренировочным примерам (25,010)
test_samples.csv   Тестовые примеры (1,000,000)
test_answers.csv   Ответы к тестовым примерам (1,000,000)

Каждый пример - описание руки в покере из пяти карт (85 атрибутов). Каждая карта описывается бинарным вектором из 17 атрибутов:
	Первые 4 значения - цвет карты (isHearts, isSpades, isDiamonds, isClubs)
	Следующие 13 значений - ранг карты (isAce, is2, is3, ... , isQueen, isKing)

Каждый ответ - тип комбинации в покере, который описывается соответственным примером. Каждый ответ описывается бинарным вектором из 10 атрибутов:
	(isNothing, isOnePair, isTwoPairs, isThreeOfAKind, isStraight, isFlush, isFullHouse, isFourOfAKind, isStraightFlush, isRoyalFlush)

0: Nothing in hand; not a recognized poker hand 
1: One pair; one pair of equal ranks within five cards
2: Two pairs; two pairs of equal ranks within five cards
3: Three of a kind; three equal ranks within five cards
4: Straight; five cards, sequentially ranked with no gaps
5: Flush; five cards with the same suit
6: Full house; pair + different rank three of a kind
7: Four of a kind; four equal ranks within five cards
8: Straight flush; straight + flush
9: Royal flush; {Ace, King, Queen, Jack, Ten} + flush