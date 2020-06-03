from random import randint

positions = (
  'First base ',
  'Second base ',
  'Shortstop ',
  'Third base ',
  'Catcher ',
  'Pitcher ',
  'Left Field ',
  'Center Field',
  'Right Field ',
)

names = ['Irregular Hexagon','Isosceles Triangle','Scalene Triangle','Irregular Square','Numpty Muffin','Ragamuffin','Muffinhead','Muffin','Custom Cursor','Slowprint','Evil Mastermind Baguette','Cold Quesadilla', 'Big fat cheater bufffff']

innings = {
  1: "first",
  2: "second",
  3: "third",
  4: "fourth",
  5: "fifth",
  6: "sixth",
  7: "seventh",
  8: "eighth",
  9: "ninth"
}

hit_score = {
  "single": 1,
  "double": 2,
  "triple": 3,
  "home run": 4
}

# return value is: (outcome, XP earned)
def swing():
  hits = randint(1,59)
  if hits >= 1 and hits <= 10:
    return ("ball", 1)
  if hits >= 11 and hits <= 20:
    return("strike", 1)
  if hits >= 21 and hits <= 26:
    return("single", 5)
  if hits >= 27 and hits <= 32:
    return("double", 8)
  if hits >= 33 and hits <= 38:
    return("triple", 15)
  if hits >= 39 and hits <= 41:
    return("home run", 20)
  if hits >= 42 and hits <=48:
    return("ground out", 1)
  if hits >= 49 and hits <=55:
    return("pop fly out", 1)
  if hits >= 56 and hits <=57:
    return("right field out", 1)
  if hits >= 58 and hits <=59:
    return("center field out", 1)

"""
This is the function that calculates the state of the bases 
(and any runs) after a hit.
"""
def calc_bases(bases, hit):
  runs = 0
  #print("Bases:",bin(bases),"Hit:", hit_score[hit], 2 ** hit_score[hit])
  newbases = (bases << hit_score[hit]) + (2 ** (hit_score[hit] - 1))
  #print("Newbases:",bin(newbases))
  for i in range(6, 2, -1):
    #print(i, newbases, bin(newbases))
    if newbases // (2 ** i):
      #print("add run")
      runs += 1 
      newbases -= (2 **i)
  return (newbases, runs)

def report_players_on_base(bases):
  if bases % 2:
    print("Man on first.")
  if (bases >> 1) % 2:
    print("Man on second.")
  if (bases >> 2) % 2:
    print("Man on third.")

# guys, we lost this! Please re-add commentary bits
commentary = [
  "Now here's a batting style you don't see everyday.",
  "If I had a nickel for every time I heard this player curse!",
  "Now here comes what some are calling the player of the year.",
  "What an isoceles triangle!",
  "Hey batter batter batter",
  "The batter stepping up to the plate needs to get their game up right now",
  "The irregular hexagon is on the plate now",
  "This batter was caught eating pizza in the dugout. They have tomato sauce all over they're shirt now",
  "The batter stepping up to plate is the player that makes their team so good",
  "Ohhhh, that's a stinky smell. You can smell it from a mile away",
]
