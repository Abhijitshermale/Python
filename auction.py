from replit import clear
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids={}

not_end=False

def find_max(bids):
  high=0
  for i in bids:

    bid_val=bids[i]
    if bid_val>high:
      high=bid_val
      winer=i
  print(f"The Winner is{winer} and its bid is {high}")


while not not_end:
  name=input("What is your Name? ")
  price=int(input("Enter Your Bid: S")) 
  bids[name]=price
  choices=input("Any One want to bid?Y/N").lower()
  if choices=="n":
    not_end=True
    find_max(bids)
  elif choices=="y":
    clear()

