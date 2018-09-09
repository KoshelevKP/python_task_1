class animal:
  
  vote = None
  feed_status = 'голодный'

  def __init__(self, name, wight):
    self.name = name
    self.wight = wight

  def feed(self):
    self.feed_status = 'сытый'

  def __lt__(self, other):
    return self.wight < other.wight

class bird(animal):

  def __init__(self, name, wight, eggs):
    super().__init__(name, wight)
    self.eggs = eggs

  def take_eggs(self):
    print(self.eggs, 'яиц')

class milk_animal(animal):

  def __init__(self, name, wight, milk):
    super().__init__(name, wight)
    self.milk = milk

  def take_milk(self):
    print(self.milk, 'л. молока')

class sheep(animal):

  def __init__(self, name, wight, wool):
    super().__init__(name, wight)
    self.wool = wool

  def take_wool(self):
    print(self.wool, 'кг. шерсти')

class goose(bird):
  
   vote = 'Га-Га'

class duck(bird):
  
   vote = 'кря-кря'

class hen(bird):
  
   vote = 'ко-ко-ко'

class cow(milk_animal):

  vote = 'муууу'
  
class goat(milk_animal):

  vote = 'бееее'


Animals = [goose('Серый', 2, 5), 
           goose('Белый', 2.5, 6),
           cow('Манька', 205, 6),
           sheep('Барашек', 45, 3),
           sheep('Кудрявый', 40, 3.5),
           hen('Ко-Ко', 1.5, 7),
           hen('Кукареку', 1.7, 8),
           goat('Рога', 25, 3),
           goat('Копыта', 30, 4),
           duck('белый', 4, 5),]

#print (Animals)

for value in Animals:
  value.feed()

Animals[0].take_eggs()
Animals[1].take_eggs()
Animals[2].take_milk()
Animals[3].take_wool()
Animals[4].take_wool()
Animals[5].take_eggs()
Animals[6].take_eggs()
Animals[7].take_milk()
Animals[8].take_milk()
Animals[9].take_eggs()


wight = 0
for value in Animals:
  wight += value.wight
print('вес всех животных', wight)

max_wight = 0
biggest_animal = ''
for value in Animals:
  if value.wight > max_wight:
    max_wight = value.wight
    biggest_animal = value.name
print('самое большое жтвотное', biggest_animal)