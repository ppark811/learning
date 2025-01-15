from IPython import get_ipython

gavel = """              
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
"""

print(gavel)
data = {}

while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    data[name] = bid
    
    goOn = input("Are there more bidders? (y/n) ")
    
    if goOn == "n":
        break
    else:
        get_ipython().magic("clear") #clears python console
    

maxBid = 0
maxBidder = ""

for bidder in data:
    if data[bidder] > maxBid:
        maxBid = data[bidder]
        maxBidder = bidder

print(f"The winner is {maxBidder} with a bid of {maxBid}")
