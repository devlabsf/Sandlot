"""
TO DO:
• Too easy to get hits; adjust values in utils.py
• Add commentary lines (there is already some but add more)
• Update all player stats in player.update_stats()
• When a game is over, there should be a banner or something with the final score
• When a game is over, team record should be updated
• When a game is over, probably should auto-save to the database
• Team Manager Menu should show team's record (wins/losses)
• Write a function to load up teams with Live Oak kids. 1 team = 10 kids. randomize their team, team number, position

"""
import time
import team
from league import *
from termcolor import colored
import sys
#import game

def intro():
  print(40 * "*")
  print("This code is a production of the DL bros".center(40,'*'))
  print(40 * "*")
  time.sleep(0.5)
  print("Harry's signature\U0001f3c6  ".center(40,'*'))
  print(40 * "*")
  time.sleep(0.5)
  print("Jayden's signature\U0001f48e  ".center(40,'*'))
  print(40 * "*")
  time.sleep(0.5)
  print("Lazlo's signature\u2b50  ".center(40,'*'))
  print(40 * "*")
  print(" ")

def menu(selectedteam):
  print(colored(40 * "*","yellow"))
  print(colored(f" TEAM MANAGER MENU ".center(40,'*'),"yellow"))
  print(colored(f" {selectedteam.name} ".center(40,'*'),"yellow"))
  print(colored(40 * "*","yellow"))
  print(colored("a. player roster", "red"))
  print(colored("b. add player", "yellow"))
  print(colored("c. cut player", "green"))
  print(colored("d. modify player profile", "blue"))
  print(colored("e. batting practice", "cyan"))
  print(colored("f. trade players", "yellow"))
  print(colored("g. go to store", "green"))
  print(colored("h. select another team", "blue"))
  print(colored("i. add new team", "cyan"))
  print(colored("j. delete team name", "yellow"))
  print(colored("k. add players in batch", "yellow"))
  print(colored("s. save", "green"))
  print(colored("q. quit", "blue"))
  print(colored(25 * "-", "red"))
  print(colored("z. PLAY BALL!", "yellow"))
  print(colored(25 * "-", "red"))

def clear():
  sys.stdout.write("\033[2J\033[H")

def save_data():
  f = open("data/league.db",'wb')
  pickle.dump(brosleague,f)
  f.close()
  
def main():
  intro()
  selectedteam = brosleague.teams[0]

  while True:
    menu(selectedteam)
    option = input("Pick one: ")
    if option in ['a','A']:
      selectedteam.print_roster()
    if option in ['b','B']:
      selectedteam.add_player()
    if option in ['c','C']:
      selectedteam.cut_player()
    if option in ['d','D']:
      print("Modify which player?" )
      for i, player in enumerate(selectedteam.players):
        print(f"{i+1}. {player.name}")
      ch = int(input("Your choice: " ))
      player = selectedteam.players[ch-1]
      player.modify()
    if option in ['e','E']:
      print("batting practice goes here")
    if option in ['f','F']:
      print("trade players")
    if option in ['g','G']:
      selectedteam.go_to_store()
    if option in ['h','H']:
      for i, t in enumerate(brosleague.teams):
        print(f"{i+1}. {t.name}")
      inter = int(input("Select which team? "))
      selectedteam = brosleague.teams[inter-1]
    if option in ['i','I']:
      teamname = input("Enter new team name: ")
      brosleague.teams.append(team.Team(teamname))
    if option in ['j','J']:
      for i, t in enumerate(brosleague.teams):
        print(f"{i+1}. {t.name}")
      delete_team = int(input("Delete which team? "))
      del brosleague.teams[delete_team - 1]
    if option in ['k','k']:
      brosleague.add_players()
      save_data()
    if option in ['q','Q']:
      yn = input("Now quitting...Save changes? (y/n) ")
      if yn in ['y','Y','yes','YES',"Yes"]:
        save_data()
      break
    if option in ['s','S']:
      save_data()
    if option in ['z','Z']:
      playgame()

if __name__ == '__main__':
  main()
 