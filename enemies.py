__author__ = 'student'
# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer
class Troll(Enemy):
    def set_answer(self,answer):
        self.__answer = answer
    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 170
        self._attack = 15
        self._color = 'красный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 250
        self._attack = 9
        self._color = 'черный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
class CleverTroll1(Troll):
    def __init__(self):
        self._health=300
        self._attack=20
        self._color='зеленый толстый тролль'
    def question(self):
        x = randint(1,5)
        self.__quest = 'Угадай число от 1 до 5!'
        self.set_answer(x)
        return self.__quest
class CleverTroll2(Troll):
    def __init__(self):
        self._health=280
        self._attack=25
        self._color='синий худой тролль'
    def question(self):
        x = randint(1,1000)
        self.__quest = 'Угадай, простое ли число'+' '+str(x)+'?'+'Простое-1,Составное-0,Ни простое, ни составное-00'
        n=0
        for y in range(1,x):
            if x%y==0:
                n+=1
        if n>2:
            self.set_answer(1)
        if n==2:
            self.set_answer(0)
        if n==1:
            self.set_answer(00)
        return self.__quest
class CleverTroll3(Troll):
    def __init__(self):
        self._health=350
        self._attack=20
        self._color='Огромный серый тролль'
    def question(self):
        x = randint(1,100)
        self.__quest = 'Разложи число'+' '+str(x)+' '+'на множители в порядке возрастания! Само число включается!'
        A=[]
        for y in range (1,x+1):
            if x%y==0:
                A.append(y)
        j=''
        for t in range(len(A)):
            j+=str(A[t])
        u=int(j)
        self.set_answer(u)
        return self.__quest

enemy_types = [GreenDragon, RedDragon, BlackDragon,CleverTroll1,CleverTroll2,CleverTroll3]
