from random import randint

outcomes = (
  "foul ball",
  "foul ball",
  "foul ball",
  "strike",
  "strike",
  "single",
  "double",
  "triple",
  "home run",
  "out",
  "out",
  "out"
)

positions = (
  'Third base ',
  'Second base ',
  'First base ',
  'Catcher ',
  'Pitcher ',
  'Left Field ',
  'Right Field ',
  'Center Field',
  'Shortstop ',
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

def swing():
  hits = randint(1,18)
  if hits >= 1 and hits <= 3:
    return ("ball", 0)
  if hits >= 4 and hits <= 6:
    return("strike", 5)
  if hits >= 7 and hits <= 9:
    return("single", 5)
  if hits >= 10 and hits <= 11:
    return("double", 6)
  if hits == 12:
    return("triple", 7)
  if hits == 13:
    return("home run", 8)
  if hits >= 14 and hits <=18:
    return("out", 0)

def calc_bases(bases, hit):
  runs = 0
  #print("Bases:",bin(bases),"Hit:", hit_score[hit], 2 ** hit_score[hit])
  newbases = (bases << hit_score[hit]) + (2 ** (hit_score[hit] - 1))
  #print("Newbases:",bin(newbases))
  # correct up to here
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
