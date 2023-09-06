""" Задание 2. (повышенной сложности). Доработать
функцию из предыдущего задания таким образом,
чтобы у нее появился дополнительный режим
работы, в котором вывод разбивается на слова
с удалением всех знаков пунктуации (их можно
взять из списка string.punctuation модуля string).
В этом режиме должно проверяться наличие
слова в выводе. """

import subprocess
import string

def command_testing(args, text):
    res = subprocess.run(args, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    words = res.stdout
    no_punctuation = words.translate(str.maketrans('', '', string.punctuation))
    list_words = no_punctuation.split()

    if text in list_words and res.returncode == 0:
        return True
    else:
        return False
    