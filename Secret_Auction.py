# Day 9 Output - Secret Auction Program
import art_works
import extra_functions

print(art_works.auction)
print("Welcome to the Py Secret Auction Program!")

bids = {}
Continue_Bidding = True
while Continue_Bidding:
    name = input("Name: ")
    price = input("Bid: ")

    bids[name] = int(price)

    replay = input("Are there other users to bid? Type yes or no ").lower()
    if replay == "yes":
        Continue_Bidding = True
        extra_functions.clearscreen()
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
