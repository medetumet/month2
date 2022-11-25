class Hero:
    def __init__(self, power=0, speed=0, hp=0, damage=0):
        self.__power = power
        self.__speed = speed
        self.__hp = hp
        self.__damage = damage

    def setpower(self, power):
        self.__power = power
    def getpower(self):
        return self.__power

    def setspeed(self, speed):
        self.__speed = speed

    def getspeed(self):
        return self. __speed

    def sethp(self, hp):
        self.__hp = hp

    def gethp(self):
        return self.__hp

    def setdamage(self, damage):
        self.__damage = damage

    def getdamage(self):
        return self.__damage


superhr = Hero()
superhr.setpower(50)
superhr.setspeed(250)
superhr.sethp(100)
superhr.setdamage(350)

print(f'сила {superhr.getpower()}\n'
      f'скорость {superhr.getspeed()}\n'
      f'жизнь {superhr.gethp()}\n'
      f'урон {superhr.getdamage()}\n')
