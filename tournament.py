__author__ = 'student'
# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    n=0
    for dragon in dragon_list:
        print('Вышел', dragon._color, '!')
        while dragon.is_alive()==True and hero.is_alive()==True:
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** враг кричит от боли **')
                hero._experience+=10
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive()==False:
            n+=1
            print('Враг', dragon._color, 'повержен!\n')

    if hero.is_alive() and n==6:
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')
        print('Ваш накопленный опыт:', hero._experience)

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами и троллями!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 6
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 6)
        print('У Вас на пути', dragon_number, 'врагов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
