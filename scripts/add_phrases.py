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

# Самые частотные разговорные фразы для жизни и работы в Турции
common_phrases = [
    # 1. Рабочие фразы в цеху и на монтаже (Schüco цех)
    ("Ne yapmam gerekiyor?", "Что мне нужно делать?", "shop_phrases", "Цеховые фразы"),
    ("Bunu nereye koyayım?", "Куда мне это положить / поставить?", "shop_phrases", "Цеховые фразы"),
    ("Yardım edebilir misin?", "Можешь помочь?", "shop_phrases", "Цеховые фразы"),
    ("Bir el atar mısın?", "Помоги перенести (подсоби руками)?", "shop_phrases", "Цеховые фразы"),
    ("Malzeme bitti", "Материал закончился", "shop_phrases", "Цеховые фразы"),
    ("Yeni parça lazım", "Нужна новая деталь / заготовка", "shop_phrases", "Цеховые фразы"),
    ("Bu parça hatalı", "Эта деталь дефектная / бракованная", "shop_phrases", "Цеховые фразы"),
    ("Ölçüleri kontrol ettin mi?", "Ты проверил размеры?", "shop_phrases", "Цеховые фразы"),
    ("İş bitti mi?", "Работа закончена?", "shop_phrases", "Цеховые фразы"),
    ("Az kaldı, bitiriyorum", "Немного осталось, заканчиваю", "shop_phrases", "Цеховые фразы"),
    ("Şimdi ne yapıyoruz?", "Что мы делаем сейчас?", "shop_phrases", "Цеховые фразы"),
    ("Bunu kim yaptı?", "Кто это сделал?", "shop_phrases", "Цеховые фразы"),
    ("Usta bakar mısın?", "Мастер, посмотри пожалуйста!", "shop_phrases", "Цеховые фразы"),
    ("Hangi alet lazım?", "Какой инструмент нужен?", "shop_phrases", "Цеховые фразы"),
    ("Bana şarjlı matkabı ver", "Передай мне шуруповерт", "shop_phrases", "Цеховые фразы"),
    ("Dikkatli ol, çok sıcak", "Будь осторожен, очень горячо!", "shop_phrases", "Цеховые фразы"),
    ("Dikkatli ol, keskin kenar", "Осторожно, острая кромка!", "shop_phrases", "Цеховые фразы"),
    ("Makineyi durdur!", "Останови станок!", "shop_phrases", "Цеховые фразы"),
    ("Hava hortumunu uzat", "Протяни пневматический шланг", "shop_phrases", "Цеховые фразы"),
    ("Yarın mesai var mı?", "Завтра будут сверхурочные?", "shop_phrases", "Цеховые фразы"),
    ("Paydos vakti geldi", "Время окончания смены (конец работы)!", "shop_phrases", "Цеховые фразы"),
    ("Yemek molası kaçta?", "Во сколько обеденный перерыв?", "shop_phrases", "Цеховые фразы"),
    ("Sigara molasına çıkıyorum", "Я выхожу на перекур", "shop_phrases", "Цеховые фразы"),
    ("Hemen geliyorum", "Я сейчас вернусь (одна минута)", "shop_phrases", "Цеховые фразы"),
    ("Bunu düzeltmem lazım", "Мне нужно это исправить / переделать", "shop_phrases", "Цеховые фразы"),
    ("Çizime göre uygun", "Сделано строго по чертежу", "shop_phrases", "Цеховые фразы"),
    ("Usta onay verdi", "Мастер одобрил / принял работу", "shop_phrases", "Цеховые фразы"),
    ("Vinç geliyor, kenara çekilin", "Кран идет, отойдите в сторону!", "shop_phrases", "Цеховые фразы"),
    ("Camı dikkatli tut", "Держи стекло осторожно!", "shop_phrases", "Цеховые фразы"),
    ("Bu profilin boyu kaç?", "Какая длина у этого профиля?", "shop_phrases", "Цеховые фразы"),
    ("Açıyı kaç derece kesiyoruz?", "Под каким углом режем?", "shop_phrases", "Цеховые фразы"),
    ("Kırk beş derece kes", "Режь под 45 градусов", "shop_phrases", "Цеховые фразы"),
    ("Doksan derece gönye", "Прямой угол (90 градусов по угольнику)", "shop_phrases", "Цеховые фразы"),
    ("Civataları iyi sık", "Затяни болты как следует", "shop_phrases", "Цеховые фразы"),
    ("Silikonu düzgün çek", "Наноси силикон ровным швом", "shop_phrases", "Цеховые фразы"),

    # 2. Повседневные и жизненные разговорные фразы (Топ турецкой речи)
    ("Nasılsınız? İyiyim, siz nasılsınız?", "Как вы? Я хорошо, а вы как?", "daily_phrases", "Разговорные фразы"),
    ("Adınız ne? Benim adım Timur", "Как вас зовут? Меня зовут Тимур", "daily_phrases", "Разговорные фразы"),
    ("Tanıştığımıza memnun oldum", "Очень приятно познакомиться", "daily_phrases", "Разговорные фразы"),
    ("Ben de çok memnun oldum", "Мне тоже очень приятно", "daily_phrases", "Разговорные фразы"),
    ("Türkçe az biliyorum", "Я немного знаю турецкий язык", "daily_phrases", "Разговорные фразы"),
    ("Biraz daha yavaş konuşur musunuz?", "Не могли бы вы говорить помедленнее?", "daily_phrases", "Разговорные фразы"),
    ("Tekrar söyler misiniz?", "Повторите еще раз, пожалуйста?", "daily_phrases", "Разговорные фразы"),
    ("Bunu anlamadım, açıklar mısınız?", "Я этого не понял, поясните пожалуйста?", "daily_phrases", "Разговорные фразы"),
    ("Bunun Türkçe adı ne?", "Как это называется по-турецки?", "daily_phrases", "Разговорные фразы"),
    ("Ne demek istiyorsunuz?", "Что вы имеете в виду?", "daily_phrases", "Разговорные фразы"),
    ("Bakar mısınız?", "Будьте добры! / Подойдите, пожалуйста!", "daily_phrases", "Разговорные фразы"),
    ("Hesap lütfen", "Счет, пожалуйста", "daily_phrases", "Разговорные фразы"),
    ("Kredi kartı geçiyor mu?", "Принимается ли оплата картой?", "daily_phrases", "Разговорные фразы"),
    ("Nakit ödeyeceğim", "Я заплачу наличными", "daily_phrases", "Разговорные фразы"),
    ("Fiş alabilir miyim?", "Можно чек / квитанцию?", "daily_phrases", "Разговорные фразы"),
    ("Poşet ister misiniz? Yok, istemiyorum", "Пакет нужен? Нет, спасибо, не надо", "daily_phrases", "Разговорные фразы"),
    ("Ne kadar tuttu?", "Сколько вышло по сумме?", "daily_phrases", "Разговорные фразы"),
    ("İndirim yapabilir misiniz?", "Сделаете скидку?", "daily_phrases", "Разговорные фразы"),
    ("En son kaç olur?", "Какая окончательная цена?", "daily_phrases", "Разговорные фразы"),
    ("Su alabilir miyim?", "Можно стакан воды?", "daily_phrases", "Разговорные фразы"),
    ("İki çay alabilir miyiz?", "Можно нам два чая?", "daily_phrases", "Разговорные фразы"),
    ("Lavabo nerede acaba?", "Подскажите, где находится туалет?", "daily_phrases", "Разговорные фразы"),
    ("Oraya nasıl gidebilirim?", "Как мне дойти / доехать туда?", "daily_phrases", "Разговорные фразы"),
    ("Otobüs durağı nerede?", "Где автобусная остановка?", "daily_phrases", "Разговорные фразы"),
    ("Metroya ne kadar uzaklıkta?", "Как далеко до станции метро?", "daily_phrases", "Разговорные фразы"),
    ("Düz gidin, sağa dönün", "Идите прямо, поверните направо", "daily_phrases", "Разговорные фразы"),
    ("Işıklardan sola dönün", "На светофоре поверните налево", "daily_phrases", "Разговорные фразы"),
    ("Yardıma ihtiyacım var", "Мне нужна помощь", "daily_phrases", "Разговорные фразы"),
    ("Bana yardım edebilir misiniz?", "Вы не могли бы мне помочь?", "daily_phrases", "Разговорные фразы"),
    ("Kendinize iyi bakın", "Берегите себя!", "daily_phrases", "Разговорные фразы"),
    ("Hayırlı işler, kolay gelsin", "Удачной работы и легкого дня!", "daily_phrases", "Разговорные фразы"),
    ("Görüşmek üzere, hoşça kalın", "До скорой встречи, всего доброго!", "daily_phrases", "Разговорные фразы"),
    ("İyi akşamlar, yarın görüşürüz", "Добрый вечер, увидимся завтра!", "daily_phrases", "Разговорные фразы"),
    ("İyi istirahatler", "Хорошего отдыха!", "daily_phrases", "Разговорные фразы"),
    ("Eline koluna sağlık", "Огромное спасибо за отличную работу!", "daily_phrases", "Разговорные фразы"),
    ("Afiyet bal şeker olsun", "Приятного аппетита (на здоровье)!", "daily_phrases", "Разговорные фразы"),
    ("Çok teşekkür ederim, sağ olun", "Большое спасибо, будьте здоровы!", "daily_phrases", "Разговорные фразы"),
    ("Bir şey değil, her zaman", "Не за что, всегда рад помочь!", "daily_phrases", "Разговорные фразы"),
    ("Kusura bakmayın, rahatsız ettim", "Извините, что побеспокоил", "daily_phrases", "Разговорные фразы"),
    ("Sorun yok, hiç önemli değil", "Все в порядке, абсолютно не важно!", "daily_phrases", "Разговорные фразы"),
    ("Merak etme, hallederiz", "Не волнуйся, мы со всем разберемся!", "daily_phrases", "Разговорные фразы"),
    ("Bana uyar, sıkıntı yok", "Мне подходит, никаких проблем!", "daily_phrases", "Разговорные фразы"),
    ("Fark etmez, nasıl istersen", "Без разницы, как захочешь", "daily_phrases", "Разговорные фразы"),
    ("Haklısınız, katılıyorum", "Вы совершенно правы, согласен", "daily_phrases", "Разговорные фразы"),
    ("Kesinlikle öyle", "Безусловно, так и есть", "daily_phrases", "Разговорные фразы"),
    ("Tabii ki, memnuniyetle", "Конечно, с большим удовольствием!", "daily_phrases", "Разговорные фразы"),
    ("Saat kaçta buluşuyoruz?", "Во сколько часов мы встречаемся?", "daily_phrases", "Разговорные фразы"),
    ("Trafik çok yoğundu, geç kaldım", "Были сильные пробки, я опоздал", "daily_phrases", "Разговорные фразы"),
    ("Hemen yola çıkıyorum", "Я уже выхожу / выезжаю в путь", "daily_phrases", "Разговорные фразы"),
    ("Hayırlı cumalar", "Благословенной пятницы!", "daily_phrases", "Разговорные фразы"),
    ("Hayırlı bayramlar", "С праздником!", "daily_phrases", "Разговорные фразы"),
    ("Geçmiş olsun, acil şifalar", "Выздоравливай скорее, скорейшего исцеления!", "daily_phrases", "Разговорные фразы"),
    ("Başınız sağ olsun", "Мои соболезнования", "daily_phrases", "Разговорные фразы"),
    ("Allah kolaylık versin", "Пусть Аллах облегчит труд!", "daily_phrases", "Разговорные фразы"),
    ("Hayırlı olsun, güle güle kullanın", "Поздравляю, пользуйтесь на радость!", "daily_phrases", "Разговорные фразы")
]

# Загружаем существующую базу из words.js
with open("words.js", "r", encoding="utf-8") as f:
    text = f.read()
    # Извлекаем JSON
    json_str = text.replace("window.DICTIONARY_DATABASE = ", "").rstrip(";\n")
    data = json.loads(json_str)

seen = {item["tr"].lower() for item in data}
added_count = 0

phrase_idx = 1
for item in common_phrases:
    tr = item[0].strip()
    ru = item[1].strip()
    cat = item[2].strip()
    lbl = item[3].strip()
    
    if tr.lower() in seen:
        continue
    seen.add(tr.lower())
    
    phon = turkish_to_phonetic(tr)
    is_sch = (cat == 'shop_phrases')
    
    data.append({
        "id": f"phr_{phrase_idx}",
        "tr": tr,
        "phonetic": phon,
        "ru": ru,
        "category": cat,
        "categoryLabel": lbl,
        "isSchueco": is_sch,
        "learned": False
    })
    phrase_idx += 1
    added_count += 1

print(f"Добавлено новых устойчивых фраз: {added_count}")
print(f"Всего слов и фраз в словаре: {len(data)}")

# Перезаписываем words.js
out_js = "window.DICTIONARY_DATABASE = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"
with open("words.js", "w", encoding="utf-8") as f:
    f.write(out_js)

print("words.js успешно дополнен разговорными и цеховыми фразами!")
