import os
import art
from art import logo

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
name = input("What is your name?: ")
bid = int(input("What is your bid?: $"))  
other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")

bidders = []  

def auction_data():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))  
    return name, bid

def auction(bidders):
    highest_bid = 0
    winner_name = ""

    for bidder in bidders:
        name_bidder, inserted_bid = bidder
        if inserted_bid > highest_bid:
            highest_bid = inserted_bid
            winner_name = name_bidder

    print(f"The winner is {winner_name} with a bid of ${highest_bid}")

if other_bidders == "yes":
    while True:   
        clear_console()
        name_bidder, inserted_bid = auction_data()
        bidders.append((name_bidder, inserted_bid))
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")
        if more_bidders == "no":
            break  
    auction(bidders)  
else:
    auction([(name, bid)])  
