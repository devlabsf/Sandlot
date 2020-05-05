class Player:

  def __init__(self, name, number, position):
    self.name = name
    self.number = number
    self.position = position
    self.hits = 0
    self.homeruns = 0
    self.xp = 0
    self.avg = 0.0
    self.likes = []

  def add_like(self, like):
    self.likes.append(like)

  def modify(self):
    ch = input("Change player name? ")
    if ch in ['y','Y','yes','YES']:
      name = input("Enter new name: ")
      self.name = name
    ch = input("Change player number? ")
    if ch in ['y','Y','yes','YES']:
      num = int(input("Enter new number: "))
      self.number = num
    ch = input("Change player position? ")
    if ch in ['y','Y','yes','YES']:
      pos = input("Enter new position: ")
      self.position = pos
    ch = input("Add a player's like? ")
    if ch in ['y','Y','yes','YES']:
      item = input("Add a new player like: ")
      self.likes.append(item)

  def rename(self, name):
    self.name = name

  """ 
  add more stats to player's display 
  """
  def stats(self):
    print("------------------------")
    print("Name:", self.name)
    print("Number:", self.number)
    print("Position:", self.position)
    print("Hits:", self.hits)
    print("Homeruns:", self.homeruns)
    print("Experience:", self.xp)


