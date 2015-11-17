__author__ = 'student'
# coding: utf-8
# license: GPLv3
from gameunit import *
class Hero (Attacker):
    def __init__(self,name):
        self._health = 100
        self._attack = 50
        self._name=name
        self._experience=0
    def attack(self,target):
        target._health -= self._attack
    def is_alive(self):
        if self._health > 0:
            return True
        else:
            return False
    def gameOver(self):
        if not Hero.is_alive(self):
            pass
