from Cards.Card import Card, Rank

# Done (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    rankcount = {}
    for card in hand:
        r = card.rank.value
        rankcount[r] = rankcount.get(r,0) + 1
    counts = sorted(rankcount.values(), reverse = True)

    suitcount = {}
    for card in hand:
        s = card.suit
        suitcount[s] = suitcount.get(s,0) + 1

    isFlush = any ( c >= 5 for c in suitcount.values())
    ranks = sorted(set(rankcount.keys()))
    if 14 in ranks:
        ranks.append(1)
        ranks = sorted(ranks)
    straightcount = 1
    isStraight = False

    for i in range(1,len(ranks)):
        if ranks[i] == ranks[i - 1] + 1:
            straightcount += 1
            if straightcount >= 5:
                isStraight = True
    if isStraight and isFlush:
        return "Straight Flush"
    if counts[0] == 4:
        return "Four of a kind"
    if counts[0] == 3 and counts[1] >= 2:
        return "Full House"
    if isFlush:
        return "Flush"
    if isStraight:
        return "Straight"
    if counts[0] == 3:
        return "Three of a kind"
    if counts[0] == 2:
        return "Two Pair"
    if counts [0] == 2:
        return "One Pair"
    return "High Card"

