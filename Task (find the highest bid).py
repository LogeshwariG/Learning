#Task (find the highest bid)
def clear():
    clear

def Highest_bid(bidding_record):
    high_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of {high_bid}")

bidding_finished = False
bidders = {}

while not bidding_finished:
    name = input("Name of the bidder: ")
    bid = int(input("bid amount: $"))
    bidders[name] =bid
    New_bidder = input("Want to add bid again? Type 'yes' or 'No'.\n" )
    if New_bidder == "no":
        bidding_finished = True
        Highest_bid(bidders)
    elif New_bidder == "yes":
        clear()
