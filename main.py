import random
class Warrior:
  def __init__(self,health):
    self.health = health

  def hit(self,target1,target2):
    while target1.health > 0:
      target1.health -= 20
      if target2 == warrior1:
        target2 = "Воин1"
      if target2 == warrior2:
        target2 = "Воин2"
      print(target2, " Напал ")
      print(target1.health, "Осталось оков здоровья")
    if target1.health == 0:
      print(target2, " Победил ")


warrior1 = Warrior(100)
warrior2 = Warrior(100)


a = int(input("Нажмите (1), для того чтобы позволить воину атаковать. Нажмите (2), для выхода из боя. "))

while a != 2:
  if a == 1:
    r = random.randint(1,3)
    if r % 2 == 0:
      warrior1.hit(warrior2,warrior1)
      a = int(input("Нажмите (1), для того чтобы позволить воину атаковать снова:"))
    else:
      warrior2.hit(warrior1,warrior2)
      a = int(input("Нажмите (1), для того чтобы позволить воину атаковать снова:"))
  else:
    print("Команда не распознана.Нажмите (1) или (2)")
    break