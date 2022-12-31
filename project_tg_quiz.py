import telebot
from requests import get



bot = telebot.TeleBot('1475141670:AAEemUm1ZzMv11E9RW1QhF_feRREVr3HDFc')
#keyboards

keyBoardMain = telebot.types.ReplyKeyboardMarkup(True, True)
keyBoardMain.row("Легкая")
keyBoardMain.row("Средняя")
keyBoardMain.row("Сложная")

keyBoardDecide = telebot.types.ReplyKeyboardMarkup(True, True)
keyBoardDecide.row("Да")
keyBoardDecide.row("Назад к выбору сложностей")

keyBoardDecideHard = telebot.types.ReplyKeyboardMarkup(True, True)
keyBoardDecideHard.row("Да!")
keyBoardDecideHard.row("Хочу домой!")
#scores
correct = 0
incorrect = 0
pos = 0
posSt = 0



@bot.message_handler(commands=['start'])
def get_command(message):
    if message.text == '/start':
        bot.send_message(message.chat.id,"""Добро пожаловать в игру History Quiz!
    Здесь мы будем 
    проверять ваши знания 
    по истории 
    и узнаем насколько вы 
    сведующий в области истории!
        """, reply_markup=keyBoardMain)


@bot.message_handler(content_types=['text'])
def get_command(mes):
    global correct
    global incorrect
    global pos
    if mes.text == "Легкая" and pos == 0 and posSt == 0:
        pos += 1
        bot.send_message(mes.chat.id,"""Вы выбрали категорию: Вторая мировая и 
Эпоха политики балансировки (Холодная Война). 
Начнем по порядку: Вторая Мировая Война
Вопрос №1""")
        keyBoardEasy = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardEasy.row("Польшу")
        keyBoardEasy.row("Чехословакию")
        keyBoardEasy.row("Францию")
        keyBoardEasy.row("СССР")

        bot.send_photo(mes.chat.id, get("https://cdni.rt.com/russian/images/2019.08/article/5d6abc37183561cd5b8b462b.jpg").content)
        bot.send_message(mes.chat.id,"1 сентября 1939 года Гитлеровская Германия вторгнулась в...", reply_markup=keyBoardEasy)
    elif mes.text == "Польшу" and pos == 1:
        correct += 1
        pos += 1
        keyBoardEasy = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardEasy.row("Бельгии и Нидерландов")
        keyBoardEasy.row("Литвы и Латвии")
        keyBoardEasy.row("Норвегии и Дании")
        keyBoardEasy.row("Великобритании и Исландии")


        bot.send_message(mes.chat.id, "Операция 'Везенбург' предполагала собой захват...", reply_markup=keyBoardEasy)
        bot.send_photo(mes.chat.id,get("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Bundesarchiv_Bild_101II-MW-5607-32%2C_Unternehmen_%22Weser%C3%BCbung%22%2C_%22Admiral_Hipper%22.jpg/250px-Bundesarchiv_Bild_101II-MW-5607-32%2C_Unternehmen_%22Weser%C3%BCbung%22%2C_%22Admiral_Hipper%22.jpg").content)
    elif mes.text == "Норвегии и Дании" and pos == 2:
        correct += 1
        pos += 1
        keyBoardEasy = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardEasy.row("М.М Попов")
        keyBoardEasy.row("Р.Я.Малиновский")
        keyBoardEasy.row("Г.К Жуков")
        keyBoardEasy.row("М.П Кирпонос")

        bot.send_message(mes.chat.id, "Героем битвы под Москвой стал...", reply_markup=keyBoardEasy)
        bot.send_photo(mes.chat.id, get("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/RIAN_archive_1417_The_examination_of_trophies.jpg/300px-RIAN_archive_1417_The_examination_of_trophies.jpg").content)
    elif mes.text == "Г.К Жуков" and pos == 3:
        correct += 1
        pos += 1
        keyBoardEasy = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardEasy.row("уничтожения танковых соеденений Федора фон Бока")
        keyBoardEasy.row("морского десанта в Новоросийск")
        keyBoardEasy.row("окружения фланговыми частями РККА")
        keyBoardEasy.row("покушения на генштаб в Берлине")
        bot.send_message(mes.chat.id, "Немецкие войска потерпели поражение в Сталинграде из за...", reply_markup=keyBoardEasy)
        bot.send_photo(mes.chat.id,get("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/RIAN_archive_44732_Soviet_soldiers_attack_house.jpg/577px-RIAN_archive_44732_Soviet_soldiers_attack_house.jpg").content)
    # Холодная война
    elif mes.text == "окружения фланговыми частями РККА" and pos == 4:
        correct += 1
        pos += 1
        keyBoardEasy = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardEasy.row("Коминтерн и ЕС")
        keyBoardEasy.row("Объедененный фронт Китая и Коминтерн")
        keyBoardEasy.row("Варшавский договор и Союзники")
        keyBoardEasy.row("Варшавский договор и НАТО")
        bot.send_message(mes.chat.id, "Основными силами противостояния в Холодной войне были...",reply_markup=keyBoardEasy)
        bot.send_photo(mes.chat.id,get("https://www.pravoslavie.ru/sas/image/102209/220983.p.jpg?0.8429387286305428").content)
    elif mes.text == "Варшавский договор и НАТО" and pos == 5:
        correct += 1
        pos += 1
        keyBoardEasy = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardEasy.row("Дорогa к Луне")
        keyBoardEasy.row("Новые Горизонты")
        keyBoardEasy.row("Союз - Аполлон")
        keyBoardEasy.row("Космическая гонка")

        bot.send_message(mes.chat.id, "'Соревнованиями' в освоении космоса назывались... ", reply_markup=keyBoardEasy)
        bot.send_photo(mes.chat.id, get("https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Semyorka_Rocket_R7_by_Sergei_Korolyov_in_VDNH_Ostankino_RAF0540.jpg/250px-Semyorka_Rocket_R7_by_Sergei_Korolyov_in_VDNH_Ostankino_RAF0540.jpg").content)
    elif mes.text == "Космическая гонка" and pos == 6:
        correct += 1
        pos += 1
        keyBoardEasy = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardEasy.row("Конец Холодной войны")
        keyBoardEasy.row("Падение комунестических режимов в Европе")
        keyBoardEasy.row("Ввод советских войск в Прагу")
        keyBoardEasy.row("Объеденение Германии")
        bot.send_message(mes.chat.id, "Падение Берлинской Стены ознаменовала...", reply_markup=keyBoardEasy)
        bot.send_photo(mes.chat.id, get("https://s0.rbk.ru/v6_top_pics/resized/590xH/media/img/7/73/755730461428737.jpg").content)
    elif mes.text == "Объеденение Германии" and pos == 7:
        correct += 1
        pos += 1
        keyBoardEasy = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardEasy.row("Обстрел Дома Советов")
        keyBoardEasy.row("Перестройка")
        keyBoardEasy.row("Октябрьского путч")
        keyBoardEasy.row("Выхода из состава СССР стран Балтики")

        bot.send_message(mes.chat.id, "Первостепенной причиной распада СССР стал(а)...", reply_markup=keyBoardEasy)
        bot.send_photo(mes.chat.id, get("https://upload.wikimedia.org/wikipedia/ru/3/31/Lowering_the_Soviet_Flag.png").content)
    elif mes.text == "Перестройка" and pos == 8:
        correct += 1
        bot.send_message(mes.chat.id, f"""Результаты легкой викторины.
Правильных ответов = {correct} 
Неправильных ответов = {incorrect}""")
        if correct > incorrect:
            bot.send_message(mes.chat.id, "Отличный результат!")
        else:
            bot.send_message(mes.chat.id, "Повезет в следущий раз!")
        bot.send_message(mes.chat.id, "Перейти к средней сложности?", reply_markup=keyBoardDecide)


    if (mes.text == "Средняя" and pos == 0) or (mes.text == "Да" and pos == 8):
        pos += 1
        bot.send_message(mes.chat.id, "Категория - Первая мировая война, Национально освободительная война")
        keyBoardMedium = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardMedium.row("Черногория")
        keyBoardMedium.row("Греция")
        keyBoardMedium.row("Албания")
        keyBoardMedium.row("Болгария")
        bot.send_message(mes.chat.id, "Назовите страну, которая не учавствовала в Первой балканской войне",reply_markup=keyBoardMedium)
        bot.send_photo(mes.chat.id,get("https://photochronograph.ru/wp-content/uploads/2018/12/73042_original.jpg").content)
    elif (mes.text == "Албания" and pos == 9) or (pos == 1):
        pos += 1
        correct += 1
        keyBoardMedium = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardMedium.row("Сараево")
        keyBoardMedium.row("Тузле")
        keyBoardMedium.row("Загребе")
        keyBoardMedium.row("Вене")
        bot.send_message(mes.chat.id, "Где был застрелен эцгерцог Австрийского престола Франц Фердинанд?",reply_markup=keyBoardMedium)
        bot.send_photo(mes.chat.id,get("https://fakeoff.org/image/resize/400/250/57/72/57724fc8555dd76f78098b91.jpg").content)
    elif (mes.text == "Сараево" and pos == 10) or (pos == 2):
        pos += 1
        correct += 1
        keyBoardMedium = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardMedium.row("План Шлиффена")
        keyBoardMedium.row("Брусиловский прорыв")
        keyBoardMedium.row("Дарданельская кампания")
        keyBoardMedium.row("Наступление Нивеля")
        bot.send_message(mes.chat.id, "Какое наступление стало самым кровавым?", reply_markup=keyBoardMedium)
        bot.send_photo(mes.chat.id,get("https://upload.wikimedia.org/wikipedia/commons/1/1d/Assaut-chemin-des-dames.jpg").content)
    elif (mes.text == "Наступление Нивеля" and pos == 11) or (pos == 3):
        pos += 1
        correct += 1
        keyBoardMedium = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardMedium.row("Битва при Витторио-Венето")
        keyBoardMedium.row("Битва на Пашендейле")
        keyBoardMedium.row("Битва за Верден")
        keyBoardMedium.row("Маас-Аргоннская наступательная операция")
        bot.send_message(mes.chat.id, "Какая битва или наступление поставила точку в войне?", reply_markup=keyBoardMedium)
        bot.send_photo(mes.chat.id, get("https://yaplakal.club/attachments/114-jpg.645/").content)
    elif (mes.text == "Битва на Пашендейле" and pos == 12) or (pos == 4):
        pos += 1
        correct += 1
        keyBoardMedium = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardMedium.row("Наймаными казаками")
        keyBoardMedium.row("Реестровыми казаками")
        keyBoardMedium.row("Сеймами")
        keyBoardMedium.row("Городовыми")
        bot.send_message(mes.chat.id, "Как назывались казаки, которые обладали привелегиями от польской власти?", reply_markup=keyBoardMedium)
        bot.send_photo(mes.chat.id, get("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/%D0%A2%D0%B8%D1%82%D1%83%D0%BB_%D1%80%D0%B5%D1%94%D1%81%D1%82%D1%80%D0%B0_%D0%92%D1%96%D0%B9%D1%81%D1%8C%D0%BA%D0%B0_%D0%97%D0%B0%D0%BF%D0%BE%D1%80%D0%BE%D0%B7%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE_1649_%D1%80%D0%BE%D0%BA%D1%83.jpg/340px-%D0%A2%D0%B8%D1%82%D1%83%D0%BB_%D1%80%D0%B5%D1%94%D1%81%D1%82%D1%80%D0%B0_%D0%92%D1%96%D0%B9%D1%81%D1%8C%D0%BA%D0%B0_%D0%97%D0%B0%D0%BF%D0%BE%D1%80%D0%BE%D0%B7%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE_1649_%D1%80%D0%BE%D0%BA%D1%83.jpg").content)
    elif (mes.text == "Реестровыми казаками" and pos == 13) or (pos == 5):
        pos += 1
        correct += 1
        keyBoardMedium = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardMedium.row("С. Мрозовецким")
        keyBoardMedium.row("Т. Костюшко")
        keyBoardMedium.row("Д. Чаплинским")
        keyBoardMedium.row("С. Бронцепольским")
        bot.send_message(mes.chat.id, "Одной из основных причин Национально освободительной войны стал конфликт Хмельницкого с...", reply_markup=keyBoardMedium)
        bot.send_photo(mes.chat.id, get("https://geomap.com.ua/images/uh5a/13/id_13_1.jpg").content)
    elif (mes.text == "Д. Чаплинским" and pos == 14) or (pos == 6):
        pos += 1
        correct += 1
        keyBoardMedium = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardMedium.row("при Корсуни")
        keyBoardMedium.row("на Желтых Водах")
        keyBoardMedium.row("под Збаражем")
        keyBoardMedium.row("под Пилявцем")
        bot.send_message(mes.chat.id,"Первой важной победой Хмельницкого стала битва...",reply_markup=keyBoardMedium)
        bot.send_photo(mes.chat.id, get("https://znaj.ua/images/2017/05/20/bytva-pid-zhovtymy-vodamy-1648-r.jpg").content)
    elif (mes.text == "на Желтых Водах" and pos == 15) or (pos == 7):
        pos += 1
        correct += 1
        keyBoardMedium = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardMedium.row("Глухов")
        keyBoardMedium.row("Батурин")
        keyBoardMedium.row("Чигирин")
        keyBoardMedium.row("Гадяч")
        bot.send_message(mes.chat.id, "С подписанием Зборовского мирного договора, столицей Гетьманщины стал город...", reply_markup=keyBoardMedium)
        bot.send_photo(mes.chat.id,get("https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/%D0%A7%D0%B8%D0%B3%D0%B8%D1%80%D0%B8%D0%BD.jpeg/250px-%D0%A7%D0%B8%D0%B3%D0%B8%D1%80%D0%B8%D0%BD.jpeg").content)
    elif (mes.text == "Чигирин" and pos == 16) or (pos == 8):
        correct += 1
        bot.send_message(mes.chat.id, f"""Результаты легкой викторины.
        Правильных ответов = {correct} 
        Неправильных ответов = {incorrect}""")
        if correct > incorrect:
            bot.send_message(mes.chat.id, "Отличный результат!")
        else:
            bot.send_message(mes.chat.id, "Повезет в следущий раз!")
        bot.send_message(mes.chat.id, "Перейти к сложному режиму?", reply_markup=keyBoardDecideHard)
    elif (mes.text == "Сложная" and pos == 0) or ("Да!" and pos == 16) or (pos == 8):
        pos += 1
        bot.send_message(mes.chat.id, "Категория - Рисорджименто, Сенгоку")
        keyBoardHard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardHard.row("42 года")
        keyBoardHard.row("46 лет")
        keyBoardHard.row("37 лет")
        keyBoardHard.row("50 лет")
        bot.send_message(mes.chat.id, "Процес объеденения Италии длился...",reply_markup=keyBoardHard)
        bot.send_photo(mes.chat.id,get("https://diletant.media/upload/medialibrary/cb6/cb6423fc2d13dd8eee4fe950b2aa9ca7.jpg").content)
    elif mes.text == "Хочу домой!":
        bot.send_message(mes.chat.id, """Добро пожаловать в игру History Quiz!
            Здесь мы будем проверять ваши знания по истории 
            и узнаем насколько вы сведующий в области истории!
            """, reply_markup=keyBoardMain)

    if (mes.text == "42 года" and pos == 1) or (pos == 17) or (pos == 9):
        pos += 1
        correct += 1
        keyBoardHard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoardHard.row("Витторио Альфери")
        keyBoardHard.row("Массимо Д’Адзельо")
        keyBoardHard.row("Даниеле Манино")
        keyBoardHard.row("Карл Альберт")
        bot.send_message(mes.chat.id, "Главным борцом за объеденение был...", reply_markup=keyBoardHard)
        bot.send_photo(mes.chat.id, get("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Arresto_di_Silvio_Pellico_e_Piero_Maroncelli_-_Carlo_Felice_Biscarra.jpg/220px-Arresto_di_Silvio_Pellico_e_Piero_Maroncelli_-_Carlo_Felice_Biscarra.jpg").content)




    elif mes.text == "Назад к выбору сложностей":
         bot.send_message(mes.chat.id, """Добро пожаловать в игру History Quiz!
    Здесь мы будем проверять ваши знания по истории 
    и узнаем насколько вы сведующий в области истории!
    """, reply_markup=keyBoardMain)


bot.polling()

#шаблоны
"""
bot.send_photo(mes.chat.id,get("").content)

bot.send_message(mes.chat.id, "",reply_markup=keyBoard)

keyBoard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyBoard.row("")
        keyBoard.row("")
        keyBoard.row("")
        keyBoard.row("")
"""


"""

"""
