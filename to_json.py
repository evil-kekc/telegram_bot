import json

ar = []

with open('cenz.txt', encoding='utf-8') as r:  # Открываем для чтения текстовый файл в кодировке utf-8
    for i in r:  # Проходим по нему циклом
        n = i.lower().split('\n')[0]  # Переводим все в нижний регистр, добавляем разделитель, слово добавляем в список с инексом 0
        if n != '':  # Проверяем, чтобы не было пустой строки
            ar.append(n)  # Добавляем в наш список

with open('cenz.json', 'w', encoding='utf-8') as e:  # Открываем для чтения файл .json в кодировке utf-8
    json.dump(ar, e)  # Функция dump позволяем записать данные в .json файл, передаем туда наш список из слов и передаем объект чтения
