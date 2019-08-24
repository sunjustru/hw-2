import json

# Сохранение в файл
def __do_file(action, filename, data=None, data_type=None):
    '''
    Метод по работе с файлами
    :param action: read or write
    :param filename: filename
    :param data: dict or string
    :data_type: JSON
    :return:
    '''

    with open(filename + '.json', action, encoding='UTF-8') as file:
        if action == 'r':
            if data_type == 'json':
                data = file.read()
                if (bool(data) is True):
                    return json.loads(data)
                else:
                    return False
            else:
                return file.read()
        elif action == 'w':
            if data_type == 'json':
                data = json.dumps(data)
            file.write(data)

# Метод вывода input с пометкой обязательное поле или нет
def _view_input(text, _sure=None):
    if _sure is not None and int(_sure) == 1:
        text = text + _view_color('warning', '(обязательное поле)')
    elif _sure is not None and int(_sure) == 0:
        text = text + '(не обязательное поле, что бы пропустить «-»)'


    return input(_view_color('question', text + '\n') + _view_color('answer', ' ответ: ')).lower().strip()

# проверяем на типы данных
def _type_per(_type, temp):
    try:
        # проверяем на корректность типа возвращённых данных
        _type(temp)
    except ValueError:
        return False
    return True

# Игра угадай где какая буква
def __guess_game(obj=None):
    _counter = 0
    break_game = False
    while obj['for_numbers']:

        _about = obj['about']
        _question = obj['question']
        _input_bool = obj['input']
        _type = obj['type']
        _required = obj['required']
        _notify = obj['notify']

        _tmp_num = obj['for_numbers'][-1]
        _current = obj['numbers'].index(_tmp_num)

        _done_numbers = obj['done_numbers']

        # Описание игры вывод пользователю
        print(_about)
        if _input_bool is True:
            # выводим input
            temp = _view_input(_question + _tmp_num, _required)

            # TODO: Использовать строчную функцию
            if temp == 'exit':
                return False
                break

            # проверяем возвращающийся тип данных
            if _type_per(_type, temp) is False:
                print(_view_color('error','Вы должны указать цифры от 1 до 16!'))
                continue

            temp = int(temp)

            if temp - 1 == _current:
                print(_view_color('win',_notify['right']))
                tmp_result = obj['result_string'].split('|')
                tmp_result[temp] = _tmp_num

                obj['result_string'] = '|'.join(tmp_result)
                obj['done_numbers'].append(_tmp_num)
                obj['for_numbers'].pop()
            else:
                print(_view_color('error',_notify['incorrect']))

            _counter += 1
    else:
        if not break_game:
            print(_view_color('win','Поздравляю с победой\nВы выиграли игру за ' + str(_counter) + ' попытки'))

def _view_print(text,lines = 1):
    #print('\n' * 0, text)
    print(text)


# Цвет текста
def _view_color(itm, text):
    if interface_color[itm] is not None:
        return ' ' + interface_color[itm][0] + text + interface_color[itm][1] + ' '


interface_color = {
    'question': ['\33[0m', '\033[0m'],
    'error': ['\33[41m', '\033[0m'],
    #'error': ['\033[91m', '\033[0m'],
    'warning': ['\33[33m', '\033[0m'],
    'answer': ['\33[100m', '\033[0m'],
    'exit': ['\33[41m', '\033[0m'],
    'win': ['\33[46m', '\033[0m']
}