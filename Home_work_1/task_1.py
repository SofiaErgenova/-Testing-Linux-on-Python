""" Задание 1. Написать функцию на Python, которой
передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда
успешно выполнена и текст найден в ее выводе
и False в противном случае. Передаваться
должна только одна строка, разбиение вывода
использовать не нужно. """

import subprocess

def command_testing(args, text):
    res = subprocess.run(args, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if text in res.stdout and res.returncode == 0:
        return True
    else:
        return False
    
