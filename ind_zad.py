#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def change_punct(chars=" !?"):
    def wrapper(func):
        def wrapped(*args):
            print(f"Входим в обёртку с символами {chars}")
            print(f"Выполняем обёртнутую функцию: {func}")
            string = args[0]
            for char in chars:
                string = string.replace(char, '-')
            print(string)
            return_str = func(string)
            print("Выходим из обёртки")
            return return_str

        return wrapped

    return wrapper


@change_punct(chars="?!:;,. ")
def rep_str(string):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
         'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
         'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
         'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
         'я': 'ya'}
    for k, v in t.items():
        string = string.replace(k, v)
    return string


if __name__ == "__main__":
    string = input("Введите строку для замены: ")
    print(f"Изменённая строка: {rep_str(string.lower())}")
