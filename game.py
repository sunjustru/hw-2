# ИГРА
# 1. Проверяем наличие сохранённых данных о пользователе в player_info.json
# 2. Если пользователь найден, предлагаем ему продолжить игру, либо добавить себя как нового пользователя и пройти процедуры заполнения анкеты
# 3. После добавления нового пользователя предлагаем сохранить данные и начинаем проверку ограничения по возрасту
# 4. В цикле запускаем игры player['games'] — пока только одна добавлена, но логика / механика проста;

__author__ = 'Буров А.С.'

import func_game as fn

# остановка игры
break_game = False

# проверяем равенство данных
def equally(a, b):
    if a == b:
        return True
    else:
        return False


# возвращаем TRUE/FALSE
def _bool(temp):
    if (temp == 'да'):
        return True
    elif (temp == 'нет'):
        return False
    else:
        return None


player = {
    'gameName': 'Игра от скуки!',
    'player': {
        'name': ['Как вас зовут? ', str, True],
        'old': ['Сколько вам лет? ', int, True],
        #вопрос, что должно возратиться, True&False — проверка обязательно заполнение поля или нет; Ограничиваем варианты ответов;
        'sex': ['Ваш пол? (м/ж)', str, True,['м','ж']],
        'pet': ['Имя питомца:', str, False],
        'hobby': ['Играть любишь? (да/нет)', bool, True, ['да','нет']],
    },
    'tools': {
        'save': ['Вы хотите сохранить настройки персонажа? (да/нет)', 'да', 'нет'],
    },
    'type': {
        int: 'целым числом!',
        bool: ['да', 'нет']
    },
    'player_info': {
    },
    #Игры
    'games': {
        0: {
            'about': 'Я задумал 4 числа от 1 - 4 и расположил их в произвольном порядке в строке. Скажите где какое?',
            'question': 'Где число — ',
            'numbers': ('4', '2','1', '3',),
            'for_numbers': ['2', '1', '4', '3',],
            'done_numbers': [],
            'result_string': '|*|*|*|*|',
            'input': True,
            'type': int,
            #fn.__guess_game — обращения к функции игры
            'fn': fn.__guess_game,
            'required': True,
            'notify': {
                'right': 'Да действительно верно!',
                'incorrect': 'Нет не верно, попробуйте ещё!'
            }
        }
    }
}

_player = player['player']
_player_exception = player['type']
_player_info = player['player_info']
_game_level = player['games']


def _player_add():
    break_game = False


    print(fn._view_color('warning', '\n## ДОБАВЛЕНИЕ НОВОГО ИГРОКА'), fn._view_color('exit', ' [exit] — выход ').rjust(30).ljust(20))

    for itm in _player:
        while not break_game:
            # вопрос
            _question = _player[itm][0]
            # тип данных, который необходимо вернуть
            _type = _player[itm][1]
            # Обязательное поле или нет True&False
            _sure = _player[itm][2]

            # выводим input
            temp = fn._view_input(_question, _sure)
            print(fn._view_color('warning', "---"))

            if temp == 'exit':
                break_game = True
                break

            if _sure == True and bool(temp) is False:
                fn._view_print(fn._view_color('error', 'Поле обязательное для заполнения!'))
                continue


            if 2 in range(len(_player[itm])-1):
                if temp in _player[itm][3][:]:
                    break
                else:
                    fn._view_print(fn._view_color('error', 'напишите (' + _player[itm][3][0] + ' или ' + _player[itm][3][1] + ')'))
                    continue

            # Если пользователь решил пропустить вопрос
            # TODO: Перенести в функцию, которая будет сохранять данные в файл
            if temp == '-' and _sure is False:
                temp = None
                break

            # Если необходимо приобразовать в буливое значение True&False
            if 'bool' in str(_type):
                _temp = _bool(temp)
                if _temp is None:
                    fn._view_print(fn._view_color('error', 'напишите (да или нет)'))
                    continue
                else:
                    temp = _bool(temp)

            try:
                # проверяем на корректность типа возвращённых данных
                _type(temp)
            except ValueError:
                fn._view_print(fn._view_color('error', 'Ответ дожен быть — ' + _player_exception[_type]))
                continue

            # Записываем значение введённых данных
            _player_info[itm] = temp
            break
    if break_game is False:
        if fn._view_input(player['tools']['save'][0]) in player['tools']['save'][1:]:
            #http://pythonicway.com/python-fileio
            fn.__do_file('w', 'player_info', _player_info, 'json')

    if _player_check() is True and break_game is not True:
        _start_game()
    else:
        print('Вы вышли из игры')
##
def _player_check():
    old = int(_player_info['old'])
    game_start = True

    if old >= 18 and old <= 90:
        return True
    elif old < 18:
        fn._view_print(fn._view_color('error', 'Ограничение по возрасту!\n'))
        return False
    elif old > 90:
        fn._view_print(fn._view_color('error', 'Игра для вашего возраста очень утамительна\n'))

        temp_question = ('Вы действительно хотите продолжить? (да/нет):',
                         'Вы хорошо подумали?? (да/нет)',)

        for itm in temp_question:
            while game_start:
                temp = fn._view_input(itm, True)

                if temp == 'да':
                    game_start = True
                    break
                elif temp == 'нет':
                    game_start = False
                    break
                elif temp == 'exit':
                    game_start = False
                    break
                else:
                    continue

    if game_start is True:
        return True
    else:
        return False

# Запускаем игры
def _start_game(level=0):
    for itm in _game_level:
        if _game_level[itm]['fn'](_game_level[itm]) is False:
            print('Вы вышли из игры')
            break

# Если данные пользователя были сохранены
user_save_profile = fn.__do_file('r', 'player_info', None, 'json')
#Если пользователь сохранён уже был то:
if bool(user_save_profile) is True:

    players = user_save_profile

    nav = """\n[1] войти под сохранённым пользователем\n[2] создать нового пользователя\n[3] выйти из игры"""

    fn._view_print(fn._view_color('warning', 'Мы нашли старые пользовательские данные\nИгрок: ' + players['name'].title() + nav))

    while True:
        temp = fn._view_input('Укажите цифру: ', True)

        # войти под сохранённым пользователем
        if temp == '1':
            _player_info = players
            if _player_check() is True:
                _start_game()
            break
        # создать нового пользователя
        elif temp == '2':
            _player_add()
            break
        # выход
        elif temp == '3':
            break
        else:
            fn._view_print(fn._view_color('error', 'Не смогли определить действие!'.upper()))

else:
    # отлов выход из игры
    if _player_add() is True:
        print('Пока')
