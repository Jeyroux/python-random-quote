import random

def quoter():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  rnd = random.randint(0, len(quotes) - 1)
  #returns quote and gets rid of newline
  print(quotes[rnd].rstrip())

if __name__== "__main__":
  quoter()
