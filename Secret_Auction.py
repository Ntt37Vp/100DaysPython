# Day 9 Output - Secret Auction Program
import art_works
from extra_functions import clearscreen

print(art_works.auction)
print("Welcome to the Py Secret Auction Program!")

bids = {}
Continue_Bidding = True
while Continue_Bidding:
    name = input("Name: ")
    price = input("Bid: ")

    bids[name] = int(price)

    replay = input("Are there other users to bid? Type Y for yes or N for no ").lower()
    if replay == "y" or replay == "yes":
        Continue_Bidding = True
        clearscreen()
    else:
        Continue_Bidding = False


for bidder in bids:
    highest_bid = 0
    winner = ""
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
print(f"Winner is {winner} with bidding amount of {highest_bid}")
