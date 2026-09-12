# -*- coding: utf-8 -*-
final_words = [
    ("Sağa dön", "Поверни направо", "top_adj", "Навигация и транспорт"),
    ("Sola dön", "Поверни налево", "top_adj", "Навигация и транспорт"),
    ("Düz git", "Иди / езжай прямо", "top_adj", "Навигация и транспорт"),
    ("Trafik ışığı", "Светофор", "top_nouns", "Навигация и транспорт"),
    ("Kavşak", "Перекресток", "top_nouns", "Навигация и транспорт"),
    ("Benzinlik", "Заправка (АЗС)", "top_nouns", "Навигация и транспорт"),
    ("Otopark", "Парковка / Стоянка", "top_nouns", "Навигация и транспорт"),
    ("Lastik", "Шина / Покрышка", "top_nouns", "Навигация и транспорт"),
    ("Fren", "Тормоз", "top_nouns", "Навигация и транспорт"),
    ("Debriyaj", "Сцепление", "top_nouns", "Навигация и транспорт"),
    ("Vites", "Коробка передач / Скорость", "top_nouns", "Навигация и транспорт"),
    ("Bagaj", "Багажник / Багаж", "top_nouns", "Навигация и транспорт"),
    ("Emniyet kemeri", "Ремень безопасности", "top_nouns", "Навигация и транспорт"),
    ("Hava durumu", "Прогноз погоды", "top_nouns", "Погода и природа"),
    ("Güneşli", "Солнечно", "top_adj", "Погода и природа"),
    ("Bulutlu", "Облачно", "top_adj", "Погода и природа"),
    ("Yağmurlu", "Дождливо", "top_adj", "Погода и природа"),
    ("Karlı", "Снежно", "top_adj", "Погода и природа"),
    ("Rüzgarlı", "Ветрено", "top_adj", "Погода и природа"),
    ("Fırtına", "Буря / Шторм", "top_nouns", "Погода и природа"),
    ("Sisli", "Туманно", "top_adj", "Погода и природа"),
    ("Buz", "Лед", "top_nouns", "Погода и природа"),
    ("Don", "Заморозки / Мороз", "top_nouns", "Погода и природа"),
    ("Gölge", "Тень", "top_nouns", "Погода и природа"),
    ("Rüzgar", "Ветер", "top_nouns", "Погода и природа"),
    ("Yağmur", "Дождь", "top_nouns", "Погода и природа"),
    ("Kar", "Снег", "top_nouns", "Погода и природа"),
    ("Güneş", "Солнце", "top_nouns", "Погода и природа"),
    ("Hava sıcaklığı", "Температура воздуха", "top_nouns", "Погода и природа"),
    ("Mutlu", "Счастливый / Радостный", "top_adj", "Самочувствие и эмоции"),
    ("Üzgün", "Грустный / Печальный", "top_adj", "Самочувствие и эмоции"),
    ("Kızgın", "Сердитый / Злой", "top_adj", "Самочувствие и эмоции"),
    ("Heyecanlı", "Взволнованный", "top_adj", "Самочувствие и эмоции"),
    ("Yorgun", "Уставший", "top_adj", "Самочувствие и эмоции"),
    ("Hasta", "Больной", "top_adj", "Самочувствие и эмоции"),
    ("Sağlıklı", "Здоровый", "top_adj", "Самочувствие и эмоции"),
    ("İyiyim", "Я в порядке / Мне хорошо", "top_adj", "Самочувствие и эмоции"),
    ("Kötüyüm", "Мне плохо", "top_adj", "Самочувствие и эмоции"),
    ("Birazdan", "Скоро / Через некоторое время", "top_daily", "Числа и время"),
    ("Demin", "Только что / Недавно", "top_daily", "Числа и время"),
    ("Zamanında", "Вовремя", "top_daily", "Числа и время"),
    ("Randevu", "Встреча по записи / Прием", "top_nouns", "Общение и дела"),
    ("Görüşme", "Переговоры / Собеседование", "top_nouns", "Общение и дела"),
    ("Toplantı", "Собрание / Планерка", "top_nouns", "Общение и дела"),
    ("Müşteri", "Клиент / Заказчик", "top_nouns", "Общение и дела"),
    ("Tedarikçi", "Поставщик", "top_nouns", "Общение и дела"),
    ("Firma", "Фирма / Компания", "top_nouns", "Общение и дела"),
    ("Ortak", "Партнер / Совладелец", "top_nouns", "Общение и дела"),
    ("Sorumlu", "Ответственный (лицо)", "top_nouns", "Общение и дела"),
    ("Görevli", "Дежурный / Служащий", "top_nouns", "Общение и дела"),
    ("Yetkili", "Уполномоченный представитель", "top_nouns", "Общение и дела"),
    ("Denetim", "Аудит / Инспекционный контроль", "top_nouns", "Общение и дела"),
    ("Şikayet", "Жалоба / Претензия", "top_nouns", "Общение и дела"),
    ("Memnuniyet", "Удовлетворенность / Довольство", "top_nouns", "Общение и дела"),
    ("Garanti", "Гарантия на конструкции", "top_nouns", "Общение и дела"),
    ("Süreç kontrolü", "Контроль производственного процесса", "top_nouns", "Производство Schüco"),
    ("Barkod", "Штрихкод на профиле", "top_nouns", "Производство Schüco"),
    ("Etiket", "Маркировочная наклейка", "top_nouns", "Производство Schüco"),
    ("Sevkiyat alanı", "Зона отгрузки готовых конструкций", "top_nouns", "Производство Schüco"),
    ("Montaj sahası", "Монтажная площадка на объекте", "top_nouns", "Производство Schüco")
]

with open("scripts/build_database.py", "r", encoding="utf-8") as f:
    content = f.read()

insertion = "\nfinal_list = " + repr(final_words) + "\n"
content = content.replace("extra_list =", insertion + "extra_list =")

loop2 = """
for item in final_list:
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
        "id": f"fin_{len(all_entries)+1}",
        "tr": tr,
        "phonetic": phon,
        "ru": ru,
        "category": cat,
        "categoryLabel": lbl,
        "isSchueco": (cat in ['quality', 'schueco', 'tools', 'glass', 'inspector', 'safety']),
        "learned": False
    })
"""

content = content.replace('print(f"Итого записей в базе данных: {len(all_entries)}")', loop2 + '\nprint(f"Итого записей в базе данных: {len(all_entries)}")')

with open("scripts/build_database.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Final additions ready!")
