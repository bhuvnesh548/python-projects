#secret aucton program 
import os
def find_highest_bidder(biddingdictionary):
    winner=""
    highestbid=0
    for bidder in biddingdictionary:
        bidamount=biddingdictionary[bidder]
        if bidamount > highestbid: 
            highestbid=bidamount
            winner=bidder
    print(f"the winner is {bidder} with a bid of ${bidamount}")
bids={}
continue_bid=True
while continue_bid:
    name=input("what is your name : ")
    amount=int(input("enter a bid amount : $"))
    bids[name]=amount
    continue_bid=input("is their any other bidders : yes or no : ").lower()
    if continue_bid=="no":
        continue_bid=False
        find_highest_bidder(bids)
    elif continue_bid=="yes":
        os.system("cls")