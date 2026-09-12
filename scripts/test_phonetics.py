# -*- coding: utf-8 -*-
import json
import re

# Правила приближенной практической русской транскрипции турецкого
def turkish_to_phonetic(text):
    # Предопределенные исключения и частые фразы
    t = text.lower()
    t = t.replace("schüco", "шуко").replace("epdm", "эпедеме")
    
    # Замены
    # Буквы
    res = []
    i = 0
    chars = list(t)
    n = len(chars)
    
    while i < n:
        c = chars[i]
        nxt = chars[i+1] if i + 1 < n else ''
        
        if c == 'c':
            res.append('дж')
        elif c == 'ç':
            res.append('ч')
        elif c == 'ğ':
            # yumuşak g: удлиняет гласную или дает й
            res.append('й' if nxt in 'ei' else '')
        elif c == 'ı':
            res.append('ы')
        elif c == 'i':
            res.append('и')
        elif c == 'ö':
            res.append('ё' if i > 0 and chars[i-1].isalpha() else 'о')
        elif c == 'ü':
            res.append('ю' if i > 0 and chars[i-1].isalpha() else 'у')
        elif c == 'ş':
            res.append('ш')
        elif c == 'j':
            res.append('ж')
        elif c == 'y':
            res.append('й')
        elif c == 'a':
            res.append('а')
        elif c == 'e':
            res.append('э' if i == 0 or chars[i-1] in ' \t\n-/' else 'е')
        elif c == 'o':
            res.append('о')
        elif c == 'u':
            res.append('у')
        elif c == 'b':
            res.append('б')
        elif c == 'd':
            res.append('д')
        elif c == 'f':
            res.append('ф')
        elif c == 'g':
            res.append('г')
        elif c == 'h':
            res.append('х')
        elif c == 'k':
            res.append('к')
        elif c == 'l':
            res.append('ль' if nxt in 'eiöü' or (i > 0 and chars[i-1] in 'eiöü') else 'л')
        elif c == 'm':
            res.append('м')
        elif c == 'n':
            res.append('н')
        elif c == 'p':
            res.append('п')
        elif c == 'r':
            res.append('р')
        elif c == 's':
            res.append('с')
        elif c == 't':
            res.append('т')
        elif c == 'v':
            res.append('в')
        elif c == 'z':
            res.append('з')
        else:
            res.append(c)
        i += 1
        
    s = "".join(res)
    # Корректировка сдвоенных мягких знаков
    s = re.sub(r'ль([аеёиоуыэюя])', r'л\1', s)
    s = re.sub(r' +', ' ', s).strip()
    return s.capitalize()

print("Тест транскрипции:", turkish_to_phonetic("Gönyesinde değil"))
