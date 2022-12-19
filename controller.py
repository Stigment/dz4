from multiprocessing.resource_sharer import stop
from unittest import result
import logger
import model
import view


def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            view.error_value()

def input_list(enter):
    
    a = input(enter)
    if '/0' in a:
        view.error_value_zerro()
    else:
        model.result_list(a)

def input_ask(enter):
    while True:
        a = input(enter)
        if a in ['y', 'Y', 'да', 'Да', 'Yes', 'yes']:
            return a
        else:
            model.init_first()

def input_operation(enter):
    while True:
        a = input(enter)
        if a in ['+', '-', '*', '/', '=']:
            return a
        else:
            view.error_value()

def operation():
    match (model.ops):
        case '+':
            model.total = model.first + model.second
        case '-':
            model.total = model.first - model.second
        case '*':
            model.total = model.first * model.second
        case '/':
            while model.second == 0:
                print('На ноль делить нельзя!')
                model.init_second()
            model.total = int(model.first / model.second)

        case _:
            view.error_value()
            logger.logger(f'{model.first} {model.ops} {model.second} = {model.total}')

def deleteElement(list, i):
    list.pop(i + 1)
    list.pop(i)

def operation2(list, i, oper):
    if list[i] == oper:
        list[i - 1] = model.opSelect.get(oper)(int(list[i - 1]), int(list[i + 1]))
        deleteElement(list, i)
        return True
    
def totalOperation(list):
    list1 = list
    list = list.replace(' ', '').strip()
    list = list.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')
    list = list.split()
    
   
    while len(list)>1:
        if '*' in list or '/' in list:
            for i in range(len(list)):
                if operation2(list, i, '*'): break
                if operation2(list, i, '/'): break

        elif '+' in list or '-' in list:
            for i in range(len(list)):
                if operation2(list, i, '+'): break
                if operation2(list, i, '-'): break 
    

    view.print_total2(list)
    logger.logger(f'{list1} = {list}')

    model.stop = True

    return stop
      


    