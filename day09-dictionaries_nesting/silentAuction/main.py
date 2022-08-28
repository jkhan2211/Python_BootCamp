bids = {}
bid_end = False



def find_the_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # Loops through key
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"The winner is {winner} with the bid amount of ${highest_bid}")



while not bid_end:
    name = input("What is your name?: ")
    price = input("What is your bid: $ ?")
    bids[name] = price
    should_cont = input("Are there any other bidders 'yes' or 'no'? \n ")
    if should_cont == "no":
        bid_end = True
    elif should_cont == "yes":
        clear()
