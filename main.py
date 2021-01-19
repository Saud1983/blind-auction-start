from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
other_bidder = True
bidders_list=[]

def auction(bidder_name, bid_value):
  new_bidder={}
  new_bidder["name"]=bidder_name
  new_bidder["bid"]=bid_value
  bidders_list.append(new_bidder)

while other_bidder:
  name = input("What's your name?\n").lower()
  bid = int(input("What is your bid? $\n"))
  auction(name, bid)
  more_biddrs = input("Are there any other bidders? 'y' for yes, 'n' for no \n").lower()
  if more_biddrs == "n":
    other_bidder = False 
  else:
    clear()

bids=0
for i in range(len(bidders_list)):
  print(bidders_list[i])
  if bidders_list[i]["bid"]>bids:
    bids=bidders_list[i]["bid"]
    hieghtest_bidder = bidders_list[i]

clear()
# print(bidders_list)
print(f"The winner is {hieghtest_bidder['name']} with a bid of {hieghtest_bidder['bid']}")