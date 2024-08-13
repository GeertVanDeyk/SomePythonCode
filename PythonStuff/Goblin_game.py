# GameObject main class from which all other types derive
class GameObject:
  class_name = ""
  desc = ""
  objects = {}
  numberofinstances = 0  
  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self
    self.count_numberofinstances()

  def get_desc(self):
    return self.class_name + '\n' + self.desc

  @classmethod
  def get_numberofinstances(cls):
      return cls.numberofinstances

  @classmethod
  def count_numberofinstances(cls):
        cls.numberofinstances += 1
        return cls.numberofinstances

# Goblin class derives from GameObject
class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
    self._desc = " a foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

# Functions defining possible actions
def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

def say(noun):
  return 'You said "{}"'.format(noun)

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed {}, the {}".format(thing.name, thing.class_name)
      else: 
        msg = "You hit {}, the {}".format(thing.name, thing.class_name)
  else:
    msg ="There is no {} here.".format(noun) 
  return msg



# Function to capture user input
def get_input():
  command = input(": ").split()
  verb_word = command[0]
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))


# Dictionary defining possible actions
verb_dict = {
  "say": say,
  "examine": examine,
  "hit": hit,
}



# Run program
goblin1 = Goblin("Gobbly")

while True:
  print('There are/is ', Goblin.get_numberofinstances(), ' goblins.')  
  get_input()
