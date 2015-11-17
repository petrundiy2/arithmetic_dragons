__author__ = 'student'
# coding: utf-8
# license: GPLv3


class Attacker:
    _health = None
    _attack = None

    def attack(self, target):
        target._health -= self._attack

    def is_alive(self):
        if self._health > 0:
            return True
        else:
            return False
