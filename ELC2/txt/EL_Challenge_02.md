# EXTENDED LEARNING CHALLENGE 2

PROBLEM: AGRAM is a card game for 2 players, using the cards from a standard 52-card pack. The dealer deals five cards to each player. The opponent player leads any card, playing it face up in the middle of the playing area. For this program the following strategy will be used to determine which card the dealer will play:
The dealer must play a card of the same suit if he can.
He plays the lowest card in that suit that is of a higher rank than the card the opponent played.
If he does not have such a card, he plays his lowest card in that suit.
If he does not have a card in that suit, he plays the lowest ranking card regardless of suit.
We guarantee there will be no ties.
INPUT: There will be 5 lines of input. Each line will contain the opponent’s lead card and the
5 cards held by the dealer. All cards will be represented by 2-character strings in value-suit
order. AH represents the ace of hearts. K, Q, J, and T will be used for king, queen, jack and 10
respectively. Note that the ace in this game has the lowest rank.
OUTPUT: For each input line print the card the dealer must play according to the strategy listed
above.

SAMPLE INPUT
SAMPLE OUTPUT

\1. 9D

\1. 5D, 2D, 6H, 9D, TD, 6H

\2. TC, AC, KC, QH, JS, TD

\3. 3D, 4H, 5C, 6S, 2D, 7H

\4. KS, TH, QC, 7H, 9H, 3H

\5. AC, AD, KH, JS, KS, QS

\2. KC

\3. 2D

\4. 3H

\5. AD


