import logger
import model


def error_value():
    logger.logger('Ошибка ввода данных')
    return print('Ошибка ввода данных')

def error_value_zerro():
    logger.logger('Ошибка ввода данных')
    return print('На ноль делить нельзя! Ошибка ввода данных')

def print_total():
    return print(f'Результат: {model.total}')

def print_total2(list):
    return print(f'Результат: {list}')