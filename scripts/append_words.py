# -*- coding: utf-8 -*-
import json
import re

def turkish_to_phonetic(text):
    t = text.lower()
    t = t.replace("schüco", "шуко").replace("epdm", "эпедеме")
    
    res = []
    i = 0
    chars = list(t)
    n = len(chars)
    
    while i < n:
        c = chars[i]
        nxt = chars[i+1] if i + 1 < n else ''
        prev = chars[i-1] if i > 0 else ''
        
        if c == 'c':
            res.append('дж')
        elif c == 'ç':
            res.append('ч')
        elif c == 'ğ':
            if prev in 'eiöü':
                res.append('й')
            elif prev in 'aıou':
                res.append('')
            else:
                res.append('')
        elif c == 'ı':
            res.append('ы')
        elif c == 'i':
            res.append('и')
        elif c == 'ö':
            res.append('ё' if prev.isalpha() and prev not in ' \t\n-/' else 'о')
        elif c == 'ü':
            res.append('ю' if prev.isalpha() and prev not in ' \t\n-/' else 'у')
        elif c == 'ş':
            res.append('ш')
        elif c == 'j':
            res.append('ж')
        elif c == 'y':
            res.append('й')
        elif c == 'a':
            res.append('а')
        elif c == 'e':
            res.append('э' if i == 0 or prev in ' \t\n-/' else 'е')
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
            res.append('ль' if (nxt in 'eiöü' or prev in 'eiöü') else 'л')
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
    s = re.sub(r'ль([аеёиоуыэюя])', r'л\1', s)
    s = re.sub(r' +', ' ', s).strip()
    return s.capitalize()

# Читаем существующий build_database.py и добавляем еще слова
# Ниже огромная коллекция частотных слов
extra_words = [
    # Цвета и покрытия
    ("Beyaz", "Белый", "top_adj", "Цвета и вид"),
    ("Siyah", "Черный", "top_adj", "Цвета и вид"),
    ("Gri", "Серый (Ral 7016 антрацит)", "top_adj", "Цвета и вид"),
    ("Kırmızı", "Красный", "top_adj", "Цвета и вид"),
    ("Mavi", "Синий", "top_adj", "Цвета и вид"),
    ("Sarı", "Желтый", "top_adj", "Цвета и вид"),
    ("Yeşil", "Зеленый", "top_adj", "Цвета и вид"),
    ("Kahverengi", "Коричневый", "top_adj", "Цвета и вид"),
    ("Turuncu", "Оранжевый", "top_adj", "Цвета и вид"),
    ("Mor", "Фиолетовый", "top_adj", "Цвета и вид"),
    ("Gümüş", "Серебристый / Серебро", "top_adj", "Цвета и вид"),
    ("Altın", "Золотой / Золото", "top_adj", "Цвета и вид"),
    ("Şeffaf", "Прозрачный", "top_adj", "Цвета и вид"),
    ("Opak", "Непрозрачный / Матовый", "top_adj", "Цвета и вид"),
    ("Renksiz", "Бесцветный", "top_adj", "Цвета и вид"),
    ("Eloksal", "Анодированный (покрытие)", "top_nouns", "Производство Schüco"),
    ("Toz boya", "Порошковая покраска", "top_nouns", "Производство Schüco"),
    ("Ral kodu", "Код цвета по шкале RAL", "top_nouns", "Производство Schüco"),
    ("Boya kalınlığı", "Толщина слоя покраски (микрон)", "top_nouns", "Производство Schüco"),

    # Геометрия, физика, статика
    ("Daire", "Круг / Окружность", "top_nouns", "Геометрия и замеры"),
    ("Kare", "Квадрат", "top_nouns", "Геометрия и замеры"),
    ("Üçgen", "Треугольник", "top_nouns", "Геометрия и замеры"),
    ("Dikdörtgen", "Прямоугольник", "top_nouns", "Геометрия и замеры"),
    ("Çapraz", "Диагональ / Крест-накрест", "top_nouns", "Геометрия и замеры"),
    ("Dikey", "Вертикальный / Вертикаль", "top_adj", "Геометрия и замеры"),
    ("Yatay", "Горизонтальный / Горизонталь", "top_adj", "Геометрия и замеры"),
    ("Paralel", "Параллельный", "top_adj", "Геометрия и замеры"),
    ("Dik", "Перпендикулярный / Прямой", "top_adj", "Геометрия и замеры"),
    ("Eksen", "Ось симметрии", "top_nouns", "Геометрия и замеры"),
    ("Merkez", "Центр / Середина", "top_nouns", "Геометрия и замеры"),
    ("Yarıçap", "Радиус", "top_nouns", "Геометрия и замеры"),
    ("Çevre", "Периметр / Окружность", "top_nouns", "Геометрия и замеры"),
    ("Hacim", "Объем", "top_nouns", "Геометрия и замеры"),
    ("Yoğunluk", "Плотность материала", "top_nouns", "Геометрия и замеры"),
    ("Mukavemet", "Прочность / Сопротивление материалов", "top_nouns", "Производство Schüco"),
    ("Statik hesap", "Статический расчет нагрузок", "top_nouns", "Производство Schüco"),
    ("Rüzgar yükü", "Ветровая нагрузка на фасад", "top_nouns", "Производство Schüco"),
    ("Kar yükü", "Снеговая нагрузка", "top_nouns", "Производство Schüco"),
    ("Deprem", "Землетрясение / Сейсмика", "top_nouns", "Производство Schüco"),
    ("Genleşme", "Тепловое линейное расширение", "top_nouns", "Производство Schüco"),
    ("Termal", "Тепловой / Термический", "top_adj", "Производство Schüco"),
    ("İzolasyon", "Изоляция / Утепление", "top_nouns", "Производство Schüco"),
    ("Yalıtım", "Тепло- и шумоизоляция", "top_nouns", "Производство Schüco"),
    ("Ses yalıtımı", "Звукоизоляция (дБ)", "top_nouns", "Производство Schüco"),
    ("Akustik", "Акустика / Акустический", "top_adj", "Производство Schüco"),
    ("Korozyon", "Коррозия / Ржавление", "top_nouns", "Производство Schüco"),
    ("Paslanmaz", "Нержавеющий (INOX / A2)", "top_adj", "Производство Schüco"),
    ("Galvaniz", "Оцинкованный", "top_adj", "Производство Schüco"),

    # Дополнительные инструменты цеха
    ("Lokma takımı", "Набор торцевых головок", "tools", "Станки и инструмент"),
    ("Cırcır anahtar", "Ключ-трещотка", "tools", "Станки и инструмент"),
    ("Açık ağız anahtar", "Рожковый гаечный ключ", "tools", "Станки и инструмент"),
    ("Yıldız anahtar", "Накидной гаечный ключ", "tools", "Станки и инструмент"),
    ("Düz tornavida", "Шлицевая отвертка (минус)", "tools", "Станки и инструмент"),
    ("Yıldız tornavida", "Крестовая отвертка (плюс)", "tools", "Станки и инструмент"),
    ("Pense", "Пассатижи / Плоскогубцы", "tools", "Станки и инструмент"),
    ("Yan keski", "Бокорезы / Кусачки", "tools", "Станки и инструмент"),
    ("Kargaburun", "Круглогубцы / Длинногубцы", "tools", "Станки и инструмент"),
    ("Maket bıçağı", "Строительный нож (канцелярский)", "tools", "Станки и инструмент"),
    ("Makas", "Ножницы по металлу", "tools", "Станки и инструмент"),
    ("Eğe", "Напильник / Рашпиль", "tools", "Станки и инструмент"),
    ("Zımpara", "Наждачная бумага (шкурка)", "tools", "Станки и инструмент"),
    ("Mengene", "Слесарные тиски", "tools", "Станки и инструмент"),
    ("İşkence", "Струбцина монтажная", "tools", "Станки и инструмент"),
    ("Su terazisi", "Строительный уровень (ватерпас)", "tools", "Станки и инструмент"),
    ("Lazer metre", "Лазерный дальномер / лазерный уровень", "tools", "Станки и инструмент"),
    ("Gönyeburun", "Угольник поверочный (90 градусов)", "tools", "Станки и инструмент"),
    ("Çekiç", "Молоток", "tools", "Станки и инструмент"),
    ("Balyoz", "Кувалда", "tools", "Станки и инструмент"),
    ("Keski", "Зубило", "tools", "Станки и инструмент"),
    ("Lehim", "Припой / Пайка", "tools", "Станки и инструмент"),
    ("Kaynak makinesi", "Сварочный аппарат", "tools", "Станки и инструмент"),
    ("Spiral / Avuç taşlama", "Болгарка (УШМ)", "tools", "Станки и инструмент"),
    ("Dekupaj testere", "Электролобзик", "tools", "Станки и инструмент"),
    ("Freze ucu", "Фреза по алюминию", "tools", "Станки и инструмент"),
    ("Testere elması", "Пильный диск (твердосплавный)", "tools", "Станки и инструмент"),
    ("Soğutma sıvısı", "Охлаждающая жидкость (СОЖ)", "tools", "Станки и инструмент"),

    # Дополнительные бытовые и разговорные слова
    ("Acıkmak", "Проголодаться", "top_verbs", "Глаголы"),
    ("Susamak", "Испытывать жажду", "top_verbs", "Глаголы"),
    ("Duş almak", "Принимать душ", "top_verbs", "Глаголы"),
    ("Tıraş olmak", "Бриться", "top_verbs", "Глаголы"),
    ("Giyinmek", "Одеваться", "top_verbs", "Глаголы"),
    ("Soyunmak", "Раздеваться", "top_verbs", "Глаголы"),
    ("Yıkamak", "Мыть / Стирать", "top_verbs", "Глаголы"),
    ("Kurulamak", "Вытирать насухо", "top_verbs", "Глаголы"),
    ("Ütülemek", "Гладить утюгом", "top_verbs", "Глаголы"),
    ("Pişirmek", "Готовить еду / Варить", "top_verbs", "Глаголы"),
    ("Satın almak", "Покупать", "top_verbs", "Глаголы"),
    ("Kira", "Арендная плата / Съем жилья", "top_nouns", "Быт и жизнь"),
    ("Ev sahibi", "Хозяин квартиры", "top_nouns", "Быт и жизнь"),
    ("Kiracı", "Арендатор / Жилец", "top_nouns", "Быт и жизнь"),
    ("Fatura ödemek", "Оплачивать коммунальные счета", "top_verbs", "Быт и жизнь"),
    ("Elektrik faturası", "Счет за свет", "top_nouns", "Быт и жизнь"),
    ("Su faturası", "Счет за воду", "top_nouns", "Быт и жизнь"),
    ("Doğalgaz", "Природный газ / Отопление", "top_nouns", "Быт и жизнь"),
    ("Aidat", "Ежемесячный сбор на обслуживание дома", "top_nouns", "Быт и жизнь"),
    ("Çarşı", "Рынок / Центр города", "top_nouns", "Быт и жизнь"),
    ("Bakkal", "Продуктовый магазин у дома", "top_nouns", "Быт и жизнь"),
    ("Manav", "Овощная лавка", "top_nouns", "Быт и жизнь"),
    ("Kasap", "Мясная лавка", "top_nouns", "Быт и жизнь"),
    ("Fırın", "Пекарня / Булочная", "top_nouns", "Быт и жизнь"),
    ("Berber", "Парикмахерская", "top_nouns", "Быт и жизнь"),
    ("Lokanta", "Столовая / Кафе", "top_nouns", "Быт и жизнь"),
    ("Çorba", "Суп", "top_nouns", "Быт и жизнь"),
    ("Pilav", "Рис / Плов", "top_nouns", "Быт и жизнь"),
    ("Döner", "Дёнер / Шаурма", "top_nouns", "Быт и жизнь"),
    ("Köfte", "Котлеты по-турецки", "top_nouns", "Быт и жизнь"),
    ("Salata", "Салат", "top_nouns", "Быт и жизнь"),
    ("Ayran", "Айран", "top_nouns", "Быт и жизнь"),
    ("Tatlı", "Сладкий / Десерт", "top_adj", "Быт и жизнь"),
    ("Acı", "Острый (перец) / Горький", "top_adj", "Быт и жизнь"),
    ("Ekşi", "Кислый", "top_adj", "Быт и жизнь"),
    ("Tuzlu", "Соленый", "top_adj", "Быт и жизнь"),
    ("Taze", "Свежий", "top_adj", "Быт и жизнь"),
    ("Bayat", "Черствый / Несвежий", "top_adj", "Быт и жизнь"),
    ("Sıcak su", "Горячая вода", "top_nouns", "Быт и жизнь"),
    ("Soğuk su", "Холодная вода", "top_nouns", "Быт и жизнь"),
    ("Çay molası", "Перерыв на чай", "top_nouns", "Быт и жизнь"),
    ("Öğle yemeği", "Обед", "top_nouns", "Быт и жизнь"),
    ("Akşam yemeği", "Ужин", "top_nouns", "Быт и жизнь"),
    ("Kahvaltı", "Завтрак", "top_nouns", "Быт и жизнь"),
    ("Afiyet olsun", "Приятного аппетита!", "top_adj", "Речевые обороты"),
    ("Eline sağlık", "Спасибо за работу! / Здоровья твоим рукам!", "top_adj", "Речевые обороты"),
    ("Çok yaşa", "Будь здоров! (при чихании)", "top_adj", "Речевые обороты"),
    ("Sen de gör", "Спасибо (ответ на «Будь здоров»)", "top_adj", "Речевые обороты"),
    ("Güle güle kullan", "Пользуйся с удовольствием!", "top_adj", "Речевые обороты"),
    ("Kendine iyi bak", "Береги себя!", "top_adj", "Речевые обороты"),
    ("İyi yolculuklar", "Счастливого пути!", "top_adj", "Речевые обороты"),
    ("Tebrikler", "Поздравляю!", "top_adj", "Речевые обороты"),
    ("Mutlu yıllar", "С Новым Годом!", "top_adj", "Речевые обороты"),
    ("İyi bayramlar", "С праздником!", "top_adj", "Речевые обороты")
]

# Обновляем build_database.py
with open("scripts/build_database.py", "r", encoding="utf-8") as f:
    code = f.read()

# Вставляем extra_words перед all_entries
insertion = "\nextra_list = " + repr(extra_words) + "\n"
pattern = "all_entries = []"
code = code.replace(pattern, insertion + "\n" + pattern)

# Добавляем цикл обработки extra_words
loop_code = """
for item in extra_list:
    tr = item[0].strip()
    ru = item[1].strip()
    cat = item[2].strip()
    lbl = item[3].strip()
    key = tr.lower()
    if key in seen:
        continue
    seen.add(key)
    phon = turkish_to_phonetic(tr)
    all_entries.append({
        "id": f"ext_{len(all_entries)+1}",
        "tr": tr,
        "phonetic": phon,
        "ru": ru,
        "category": cat,
        "categoryLabel": lbl,
        "isSchueco": (cat in ['quality', 'schueco', 'tools', 'glass', 'inspector', 'safety']),
        "learned": False
    })
"""

code = code.replace('print(f"Итого записей в базе данных: {len(all_entries)}")', loop_code + '\nprint(f"Итого записей в базе данных: {len(all_entries)}")')

with open("scripts/build_database.py", "w", encoding="utf-8") as f:
    f.write(code)

print("build_database.py успешно дополнен!")
