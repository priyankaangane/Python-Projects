import random
import os
import art
print(art.logo)
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
user_cards = []
computer_cards = []
game_over = False
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")
if user_score == 0 or user_score > 21 or computer_score == 0:
    game_over = True

    
while not game_over:
    new_card = input("Do you want to draw another card? if yes type 'y' if no type 'n'")

    if new_card == "y":
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        if user_score > 21:
            game_over = True
    else:
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            print(f"Computer's cards: {computer_cards}, current score: {computer_score}")
        game_over = True
result = ""

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "You lose. Computer has a Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Computer went over. You win"
    else:
        if user_score > computer_score:
            return "You win"
        else:
            return "You lose"
result = compare(user_score, computer_score)
print(result)
print("do you want to restart the game? if yes type 'y' if no type 'n'")
restart = input()
if restart == "y":
  os.system('cls')  # Clear the console
  print(art.logo)
  