import telebot
from telebot import types

# Создаем объект бота
bot = telebot.TeleBot("6753603635:AAHt7thAhzA3Y78WYC6u43swdOLjzyOmZbQ")

# Обработчик команды "/start"
@bot.message_handler(commands=['start'])
def start_message(message):
    # Создаем клавиатуру с кнопками
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Первая строка кнопок
    row1_buttons = [types.KeyboardButton(text="Серебреные Мечи"), types.KeyboardButton(text="Стальные Мечи")]
    keyboard.row(*row1_buttons)
    
    # Вторая строка кнопок
    row2_buttons = [types.KeyboardButton(text="Броня"), types.KeyboardButton(text="Плотва")]
    keyboard.row(*row2_buttons)
    
    # Третья строка кнопок
    row3_buttons = [types.KeyboardButton(text="Достижения")]
    keyboard.row(*row3_buttons)

    # Отправляем приветственное сообщение и инструкции
    welcome_message = "Здравствуйте мои маленькие любители экстремизма"
    bot.send_message(message.chat.id, welcome_message, reply_markup=keyboard)
    return keyboard

@bot.message_handler(func=lambda message: message.text.lower() == "меню")
def show_menu(message):
    keyboard = create_keyboard()
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=keyboard)

def create_keyboard():
     # Создаем клавиатуру с кнопками
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Первая строка кнопок
    row1_buttons = [types.KeyboardButton(text="Серебреные Мечи"), types.KeyboardButton(text="Стальные Мечи")]
    keyboard.row(*row1_buttons)
    
    # Вторая строка кнопок
    row2_buttons = [types.KeyboardButton(text="Броня"), types.KeyboardButton(text="Плотва")]
    keyboard.row(*row2_buttons)
    
    # Третья строка кнопок
    row3_buttons = [types.KeyboardButton(text="Достижения")]
    keyboard.row(*row3_buttons)

    # Отправляем приветственное сообщение и инструкции
    welcome_message = "Здравствуйте мои маленькие любители экстремизма"
    return keyboard
    
# Список с информацией о серебряных мечах
silver_swords_info = [
    {"name": "МЕЧ АРОНДИТ", "description": "Особенности: Клинок был списан с великого Экскалибура, принадлежащего королю Артуру. Имеет только две ключевые особенности, при этом не владеет повышающими характеристики чертами. Кроме того, только у этого клинка есть постоянно увеличивающийся базовый урон. Меч присутствует во всех частях саги. Для использования необходим 80 уровень. Как получить: оружие нельзя выковать. Оно получается в подарок от Владычицы Озера за то, что Геральт помог ей в ходе квеста «Пути Предназначения». Должно быть куплено DLC «Кровь и Вино».", "image_path": "1-2.jpg"},
    {"name": "МЕЧ КАНТАТА", "description": "Особенности: Один из самых редких клинков в игре. Обладает самыми сильными боевыми эффектами в игре одновременно: кровотечением и оглушением. Является серебряным аналогом стального меча из Хен Гайдт. Для использования необходим 80 уровень. Как получить: начать квест «Между мирами», и в ходе его прохождения в локации Хен Гайдт возле тела чародея Жана подобрать этот клинок. Должно быть куплено DLC «Кровь и Вино».", "image_path": "3-4.jpg"},
    {"name": "МЕЧ ГЕШЕФТ", "description": "Особенности: Клинок, из-за которого часто возникают путаницы. Дело в том, что в игре есть два меча с таким названием. Один можно получить в Стране Сказок, другой создается по чертежам. Сейчас речь идет именно о первом клинке. Для использования необходим 45 уровень. Как получить: победить облачного великана, но не отправляться в его замок. Пройти за блуждающим белым огоньком в пещеру, где будет находиться воткнутый в костер меч (отсылка на Dark Souls). Должно быть куплено DLC «Кровь и Вино».", "image_path": "5-6.jpg"},
    {"name": "МЕЧ САРРИМ", "description": "Особенности: Объединяет в себе черты неплохого магического и обычного оружия. Хорошо подходит для смешанных билдов. Для использования необходим 35 уровень. Как получить: создать с помощью чертежа, который выпадает случайным образом во время путешествий Геральта по Драконьей долине. Например, его можно отыскать в руинах Килкеринна. Должно быть куплено DLC «Каменные сердца».", "image_path": "7-8.jpg"},
    {"name": "МЕЧ ТОР ЗИРАЭЛь", "description": "Особенности: Этот клинок обладает очень редкой характеристикой, на которую многие игроки и вовсе не обращают внимания. Но на практике 2-х процентный шанс мгновенного убийства как нельзя лучше сочетается с серебряным мечом и дает вам возможность расправиться практически с любым противником, независимо от его уровня. Все, что вам нужно сделать - это продержаться в бою до того момента, пока перк не сработает. В среднем это происходит каждый 50-й удар, но не исключен вариант, что вы сможете сокрушить какого-нибудь огромного циклопа первым же касанием. Нужно отметить, что этот эффект срабатывает не на всех видах монстров. Во время проведенного нами эксперимента великаны и главоглазы без проблем получали по 70 000 урона от одного удара ( использовался меч 5-го уровня), а вот тролли и бесы как-будто обладали иммунитетом к этому эффекту и никак не реагировали на сотни нанесенных им ударов.", "image_path": "9-10.jpg"}
]

# Обработчик для кнопки "Серебреные Мечи"
@bot.message_handler(func=lambda message: message.text == "Серебреные Мечи")
def send_silver_swords(message):
    # Отправляем информацию о первом мече
    send_silver_sword_info(message.chat.id, 0)

# Функция для отправки информации о серебряном мече
def send_silver_sword_info(chat_id, index):
    if 0 <= index < len(silver_swords_info):
        sword = silver_swords_info[index]
        # Создаем inline-клавиатуру с кнопками "Следующий меч" и "Предыдущий меч"
        keyboard = types.InlineKeyboardMarkup()
        prev_button = types.InlineKeyboardButton("Предыдущий меч", callback_data=f"prev_sword_{index}")
        next_button = types.InlineKeyboardButton("Следующий меч", callback_data=f"next_sword_{index}")
        keyboard.row(prev_button, next_button)
        # Отправляем информацию о мече и inline-клавиатуру
        bot.send_message(chat_id, f"Название: {sword['name']}\n{sword['description']}", reply_markup=keyboard)
        # Отправляем картинку меча
        with open(sword['image_path'], 'rb') as photo:
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Нет больше мечей.")

# Обработчик для кнопок "Следующий меч" и "Предыдущий меч" серебряный
@bot.callback_query_handler(func=lambda call: call.data.startswith("prev_sword_") or call.data.startswith("next_sword_"))
def callback_silver_sword(call):
    chat_id = call.message.chat.id
    index = int(call.data.split("_")[2])
    if call.data.startswith("prev_sword_"):
        send_silver_sword_info(chat_id, index - 1)
    elif call.data.startswith("next_sword_"):
        send_silver_sword_info(chat_id, index + 1)

# Список с информацией о стальных мечах
steel_swords_info = [
    {"name": "Хен Гайдт/Тесхам Мутна (320-392)", "description": "Стальные мечи Хен Гайдт и Тесхам Мутна имеют идентичные характеристики. Как и предыдущие герои обзора, они увеличивают шанс и урон критического удара, а также с 15-процентной вероятностью накладывают на противников негативные эффекты (в данном случае кровотечение и оглушение). Но здесь присутствует еще один важный в сражениях с людьми параметр - пробитие доспеха. Оба клинка будут игнорировать 150 единиц вражеской брони, что позволит существенно увеличить наносимый вами урон. Единственное различие этих клинков состоит в том, что меч из Тесхам Мутна имеет фиксированный 39-й уровень, а у меча из Хен Гайдт уровень динамический с минимальным значением 40, что серьезно расширяет диапазон его применения. Стальной меч из Тесхам Мутна вы найдете во время выполнения сюжетного квеста «Отзвук» из дополнения «Кровь и вино». Внимательно обыскивайте подземелья древней вампирской крепости, в которой вы окажетесь вместе с Регисом - в дополнение к мечу вы найдете полный комплект брони. Клинок из Хен Гайдт также можно получить во время прохождения дополнения «Кровь и вино», но при определенном развитии событий. Если вы решите встретиться со Скрытым, то сможете получить доступ к квесту «Между мирами». Внимательно исследуете древние пещеры, и вы получите все элементы снаряжения из Хен Гайдт, включая стальной меч.", "image_path": "11-12.jpg"},
    {"name": "Витис(368-450)", "description": "Не хотелось в этом обзоре упоминать мечи, которые вместо собственной разрушительной мощи усиливают магические способности персонажа, но один из таких клинков выделить все-таки стоит. Витис отлично подойдет для игроков, которые предпочитают холодному оружию ведьмачьи знаки. Обнажив этот меч, вы получите прибавку в 20% к силе Аарда, Игни, Квена, Ирдена и Аксия. Три слота для рун позволят использовать Витис не только как усилитель знаков, но и по его прямому назначению.По сюжету меч Витис можно получить во время прохождения квеста «Страна тысячи сказок» (дополнение «Кровь и вино»), если пойти за блуждающим огоньком возле Башни Долговласки (Ранпуцель). Уровень у этого клинка также динамический, но не может быть ниже 40-го, так что поиграть им в начале игры не удастся.", "image_path": "13-14.jpg"},
    {"name": "Бельхавенский Клинок(364-444)", "description": "Начинаем знакомство с действительно мощными стальными мечами. Открывает этот список Бельхавенский клинок, предлагающий нам дополнительные 100% к урону при критическом ударе (это максимальный показатель в игре, если не брать в расчет меч Хьялмара), а также +15% к шансу нанести такой удар. В комплекте идут солидные 15% к шансу отравить противника, а также три слота под руны, что в совокупности позволит практически беспрерывно накладывать на врагов негативные эффекты. Для некоторых окажется полезным и 30-процентное усиление знака Аард. Получить чертеж Бельхавенского клинка можно только во время прохождения дополнения «Кровь и вино». Он находится в сундуке на дне реки Сансретур, протекающей в восточной части локации Туссент. Сундук с чертежом заперт, но ключ от него находится неподалеку, в лагере разбойников на восточном берегу. Разобравшись с бандитами, вы найдете записку и ключ, после чего активируется задание «В ожидании Го и До», которое укажет вам путь к затопленному сундуку.", "image_path": "15-16.jpg"},
    {"name": "Меч Хьялмара (346-424)", "description": "Этот клинок ни за что не попал бы в данный обзор, если бы ни не обладал одной уникальной характеристикой. Здесь всего один слот для рун и практически отсутствуют какие-либо бонусы, но это единственный в игре меч, увеличивающий урон при критическом ударе на 200%. Конечно, придется подтянуть шанс критического удара другими средствами, поскольку этот параметр клинок не улучшает, но если вы поднимете его хотя бы до 20%, то каждый пятый удар, нанесенный этим оружием, может стать поистине сокрушительным. Получить стальной меч Хьялмара можно в ходе выполнения сюжетного квеста «Королевский гамбит» (Скеллиге). Нужно будет в кулачном бою победить одного из вильдкаарлов, после чего Хьялмар вручит вам свой клинок. Главный нюанс состоит в том, что бонус к критическому урону у меча рандомный и определяется в тот момент, когда вы получаете оружие. Для того, чтобы выбить максимальный показатель бонуса, придется сохраниться перед самым получением меча, а затем десяток-другой раз загрузиться.", "image_path": "17-18.jpg"},
    {"name": "Меч Туссентского рыцаря(385-471)", "description": "Вот мы и подобрались к мечу, которому смело можно отдать звание лучшего стального оружия в игре «Ведьмак 3: Дикая Охота». За счет показатели пробития доспеха в 300 единиц, этот клинок будет игнорировать большую часть брони даже очень сильных соперников. Максимально прокачанный критический удар с повышением шанса на 20% и урона на 100% дополняется 15-процентной вероятностью поджечь противника. Три слота для установки рун позволят усилить и без того впечатляющие характеристики, а 30-процентное усиление знака Квен будет не самым необходимым, но вполне приятным дополнением. Если вы затаили обиду на городских стражников, то с этим мечом у вас наконец появится реальный шанс им отомстить.Чертеж стального меча туссентского рыцаря можно найти в убежище Ганзы на северной окраине Туссента. Разбойники обосновались в руинах дворца Галлион. Поднявшись на полуразрушенный мост, ищите небольшую деревянную лестницу, ведущую на второй этаж. Воспользовавшись ведьмачьим чутьем, наверху вы без труда отыщете чертеж.", "image_path": "19-20.jpg"}
]

# Обработчик для кнопки "Стальные Мечи"
@bot.message_handler(func=lambda message: message.text == "Стальные Мечи")
def send_steel_swords(message):
    # Отправляем информацию о первом стальном мече
    send_steel_sword_info(message.chat.id, 0)

# Функция для отправки информации о стальном мече
def send_steel_sword_info(chat_id, index):
    if 0 <= index < len(steel_swords_info):
        sword = steel_swords_info[index]
        # Создаем inline-клавиатуру с кнопками "Следующий меч" и "Предыдущий меч"
        keyboard = types.InlineKeyboardMarkup()
        prev_button = types.InlineKeyboardButton("Предыдущий меч", callback_data=f"prev_steel_{index}")
        next_button = types.InlineKeyboardButton("Следующий меч", callback_data=f"next_steel_{index}")
        keyboard.row(prev_button, next_button)
        # Отправляем информацию о мече и inline-клавиатуру
        bot.send_message(chat_id, f"Название: {sword['name']}\n{sword['description']}", reply_markup=keyboard)
        # Отправляем картинку меча
        with open(sword['image_path'], 'rb') as photo:
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Нет больше стальных мечей.")

# Обработчик для кнопок "Следующий меч" и "Предыдущий меч"
@bot.callback_query_handler(func=lambda call: call.data.startswith("prev_steel_") or call.data.startswith("next_steel_"))
def callback_steel_sword(call):
    chat_id = call.message.chat.id
    index = int(call.data.split("_")[2])
    if call.data.startswith("prev_steel_"):
        send_steel_sword_info(chat_id, index - 1)
    elif call.data.startswith("next_steel_"):
        send_steel_sword_info(chat_id, index + 1)

    # Список с информацией о комплектах брони
armor_sets_info = [
    {"name": "Снаряжение Школы Волка", "description": "Родная школа Геральта, что для многих игроков делает этот доспех наиболее желанным, в сравнении с другим ведьмачьим снаряжением. Внешний вид доспеха также довольно неплох, особенно у мастерского и гроссмейстерского комплектов. Давайте рассмотрим дополнительные характеристики и бонусы, которые отличают снаряжение Школы Волка от аналогичных по уровню комплектов других школ. Бонусы за сбор комплекта довольно сомнительные, да и работают они только для гроссмейстерского снаряжения, которое вы сможете получить только в дополнении «Кровь и вино», поэтому мы не уделяем им особого внимания. Получив 3 элемента комплекта, вы сможете наносить на мечи до 3-х различных масел за раз, а полный комплект даст вам возможность бросать бомбы без задержки.", "image_path": "21-22.jpg"},
    {"name": "Снаряжение Школы Кота", "description": "Сет Кота также очень популярен среди игроков, по большей части благодаря тому, что это единственный ведьмачий комплект, относящийся к классу легких доспехов. Эта характеристика позволяет вашему персонажу быстрее восстанавливать энергию, затраченную на перемещение, кувырки и применение ведьмачьих знаков. Но это конечно не все. Давайте взглянем на характеристики и попытаемся понять, чем же еще снаряжение Школы Кота заслужило внимание такого большого количества игроков. Бонусы за сбор комплекта здесь поинтереснее, чем в случае со Школой Волка: при владении 3-мя элементами гроссмейстерского снаряжения ваша мощная атака будет увеличивать урон от быстрых атак в течение 5 секунд на 10% за каждый элемент комплекта. Полный комплект (без арбалета) увеличит урон от атак в спину на 50% и, при этом, они будут оглушать противника (расходуется 1 очко адреналина).", "image_path": "23-24.jpg"},
    {"name": "Снаряжение Школы Грифона", "description": "Снаряжение Школы Грифона занимает третье место по популярности среди игроков «Ведьмак 3: Дикая Охота». Отчасти потому, что имеет самый низкий «порог вхождения» - начальный комплект доступен уже на 11 уровне персонажа, в отличие от «Волка» и «Кота», в которые можно облачиться только начиная с 14 и 17 уровней соответственно. Но все-таки, главная причина популярности «Грифона» скрыта в его дополнительных характеристиках. Бонусы за комплектность также ориентированы на усиление Знаков. Три элемента гроссмейстерского снаряжения дают возможность в течение 3-х секунд после наложения Знака использовать следующий Знак без затрат энергии (работает для стандартного режима). Полный комплект прокачивает Знак Ирден: увеличивает размер ловушки на 40% и, пока Геральт находится внутри, ускоряет восстановление энергии на 5 единиц в секунду, увеличивает мощь других знаков на 100% и снижает урон на 20%.", "image_path": "25-26.jpg"},
    {"name": "Снаряжение Школы Медведя", "description": "Комплекты Школы Медведя игроки используют гораздо реже, чем три предыдущих. Отчасти это объясняется тем, что начальное снаряжение можно использовать только с 20-го уровня, который соответствует примерно половине прохождения основной части игры. Также не всех привлекают единственные среди ведьмачьего снаряжения тяжелые доспехи, при использовании которых замедляется восстановление энергии. Однако, свои преимущества у этого снаряжения также должны быть. Давайте попытаемся отыскать их в подробных характеристиках. Единственная проблема может возникнуть с применением Знаков, т.к. зачастую у вас просто не найдется энергии для их применения, а восстановление потребует длительного бездействия. Немного ситуацию исправляют бонусы за комплектность для гроссмейстерского снаряжения. Владея тремя элементами доспеха, вы получите шанс без затрат энергии наложить новый Знак Квен, когда спадет старый (5% за каждый элемент). Полный комплект увеличит урон всех связанных с Квеном способностей на 200%.", "image_path": "27-28.jpg"},
    {"name": "Снаряжение Школы Змеи", "description": "Комплект снаряжения Школы Змеи игроки могут получить во время прохождения дополнения «Каменные сердца». Требуемый уровень у него на единицу ниже, чем у других гроссмейстерских доспехов, но это ни в коем случае не делает это снаряжение хуже, или слабее. В первую очередь «Змея» выделяется своим дизайном - доспехи практически идентичны тем, в которых вы начинаете игру (они же красуются на обложке игры). Как и в случае со Школой Мантикоры, у комплекта присутствует своя уникальная «фишка». Никаких бонусов за комплектность для снаряжения Школы Змеи не предусмотрено, но они, по сути, и не нужны. Сами доспехи уже обеспечивают вам 100% защиту от всех ядов. А учитывая, сколько раз по ходу игры Геральта травят различные монстры и растения, это свойство окажется чрезвычайно полезным.", "image_path": "29-30.jpg"},
    {"name": "Снаряжение Школы Мантикоры", "description": "Снаряжение Школы Мантикоры представлено только гроссмейстерским комплектом и становится доступно при прохождении дополнения «Кровь и вино». Как и другие гроссмейстерские комплекты требует как минимум 40-й уровень персонажа. По весу доспех является средним, так что и этим параметром не выделяется, но в перечне характеристик есть бонусы, которые делает его уникальным. Если в других Школах бонусы за комплектность были практически бесполезными, то здесь в них скрыта главная «фишка». Три элемента снаряжения активируют распространение критических эффектов на бомбы, а полный комплект повышает число зарядов всех алхимических предметов (бомб и эликсиров) на 1. При этом сами доспехи повышают максимальный уровень интоксикации на 30 единиц. Усилив предложенные бонусы соответствующими навыками персонажа, можно превратить Геральта в что-то вроде «алхимика-бомбардира» и испробовать совершенно новую тактику боя.", "image_path": "31-32.jpg"}
]

# Обработчик для кнопки "Броня"
@bot.message_handler(func=lambda message: message.text == "Броня")
def send_armor_sets(message):
    # Отправляем информацию о первом комплекте брони
    send_armor_set_info(message.chat.id, 0)

# Функция для отправки информации о комплекте брони
def send_armor_set_info(chat_id, index):
    if 0 <= index < len(armor_sets_info):
        armor_set = armor_sets_info[index]
        # Создаем inline-клавиатуру с кнопками "Следующий комплект" и "Предыдущий комплект"
        keyboard = types.InlineKeyboardMarkup()
        prev_button = types.InlineKeyboardButton("Предыдущий комплект", callback_data=f"prev_armor_{index}")
        next_button = types.InlineKeyboardButton("Следующий комплект", callback_data=f"next_armor_{index}")
        keyboard.row(prev_button, next_button)
        # Отправляем информацию о комплекте брони и inline-клавиатуру
        bot.send_message(chat_id, f"Название: {armor_set['name']}\n{armor_set['description']}", reply_markup=keyboard)
        # Отправляем картинку комплекта брони
        with open(armor_set['image_path'], 'rb') as photo:
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Нет больше комплектов брони.")

# Обработчик для кнопок "Следующий комплект" и "Предыдущий комплект"
@bot.callback_query_handler(func=lambda call: call.data.startswith("prev_armor_") or call.data.startswith("next_armor_"))
def callback_armor_set(call):
    chat_id = call.message.chat.id
    index = int(call.data.split("_")[2])
    if call.data.startswith("prev_armor_"):
        send_armor_set_info(chat_id, index - 1)
    elif call.data.startswith("next_armor_"):
        send_armor_set_info(chat_id, index + 1)

# Обработчик для кнопки "Плотва"
@bot.message_handler(func=lambda message: message.text == "Плотва")
def send_boats_info(message):
    # Отправляем информацию о первом элементе снаряжения для плотвы
    send_boat_info(message.chat.id, 0)

# Список с информацией о снаряжении для плотвы
boats_info = [
    {"name": "Шоры для плотвы", "description": "Шоры специально разработаны для комфортного и безопасного путешествия на плотве. Они обеспечивают отличную защиту от воды и ветра, позволяя плотве двигаться быстрее. Этот компонент снаряжения для плотвы позволит вам быстро и уверенно передвигаться по водной поверхности, особенно в условиях плохой погоды. Лучшие Шоры: Шоры Пяти Добродетелей, Шоры странствующего рыцаря, Шоры из Каэд Мырквида, Боклерские шоры, Туссентские шоры, Виноградные шоры, все они имеют тревогу 60,ниже представлены картинки в таком же порядке:", "image_path": "33.jpg"},
    {"name": "Седло для плотвы", "description": "Седло для плотвы создано из прочных материалов и обеспечивает удобное сиденье для плотвы. Это седло позволит вам комфортно перемещаться по воде и контролировать плотву. Оно также обладает регулируемыми ремнями, чтобы обеспечить надежную посадку. Лучшее седло - Чепрак скорби. Лучшее в игре седло — Черпак скорби — можно получить в ходе прохождения основной сюжетной линии дополнения «Каменные сердца». Имеют энергию - 100. Для получения нужно отказаться от положительного сценария развития событий и выбрать в диалоге выбора награды вариант «Хочу быть быстрым, как ветер».", "image_path": "34.jpg"},
    {"name": "Сумки для плотвы", "description": "Сумки для плотвы предназначены для перевозки грузов и снаряжения. Они имеют множество отделений и карманов, что позволяет удобно организовать хранение и перевозку ваших вещей. Этот компонент снаряжения для плотвы позволит вам взять с собой необходимое снаряжение во время водных путешествий. Лучшая сумка в игре - Боклерские вьюки, имеют объем 110 ", "image_path": "35.jpg"},
]

# Функция для отправки информации о снаряжении для плотвы
def send_boat_info(chat_id, index):
    if 0 <= index < len(boats_info):
        boat = boats_info[index]
        # Создаем inline-клавиатуру с кнопками "Следующий элемент" и "Предыдущий элемент"
        keyboard = types.InlineKeyboardMarkup()
        prev_button = types.InlineKeyboardButton("Предыдущий элемент", callback_data=f"prev_boat_{index}")
        next_button = types.InlineKeyboardButton("Следующий элемент", callback_data=f"next_boat_{index}")
        keyboard.row(prev_button, next_button)
        # Отправляем информацию о снаряжении и inline-клавиатуру
        bot.send_message(chat_id, f"Название: {boat['name']}\n{boat['description']}", reply_markup=keyboard)
        # Отправляем картинку снаряжения
        with open(boat['image_path'], 'rb') as photo:
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Нет больше элементов снаряжения для плотвы.")

# Обработчик для кнопок "Следующий элемент" и "Предыдущий элемент"
@bot.callback_query_handler(func=lambda call: call.data.startswith("prev_boat_") or call.data.startswith("next_boat_"))
def callback_boat(call):
    chat_id = call.message.chat.id
    index = int(call.data.split("_")[2])
    if call.data.startswith("prev_boat_"):
        send_boat_info(chat_id, index - 1)
    elif call.data.startswith("next_boat_"):
        send_boat_info(chat_id, index + 1)
# Список с информацией о достижениях
achievements_info = {
    "Достижение 1": "Описание достижения 1",
    "Достижение 2": "Описание достижения 2",
    # Добавьте остальные достижения
}

# Обработчик для команды "/achievements" и текста пользователя
@bot.message_handler(func=lambda message: message.text.lower() == "достижения")
def process_achievements(message):
    keyboard = types.ReplyKeyboardRemove()  # Убираем клавиатуру
    bot.send_message(message.chat.id, "Введите название достижения, 'Скрытые' для списка всех скрытых достижений, либо слово 'меню' для возвращения в главное меню.", reply_markup=keyboard)
    bot.register_next_step_handler(message, process_achievement_name)

@bot.message_handler(func=lambda message: True)
def process_achievement_name(message):
    achievement_name = message.text.lower()  # Преобразуйте текст в нижний регистр
    if achievement_name == "скрытые":
        hidden_achievements = [
           "Название достижения: Necromancer / Некромантия",
           "Название достижения: Assassin of Kings / Убийца королей",
           "Название достижения: Full Crew / В полном составе",
           "Название достижения: Friends With Benefits / Мор, колдунья и старая башня",
           "Название достижения: Kingmaker / Творец королей",
           "Название достижения: Triple Threat / Диверсификация",
           "Название достижения: What Was That? / Что это было? ",
           "Название достижения: Shrieker / Клекотун",
           "Название достижения: Fearless Vampire Slayer / Неустрашимый охотник на вампиров",
           "Название достижения: Woodland Spirit / Дух Леса",
           "Название достижения: Fiend or Foe? / Друг или враг?",
           "Название достижения: Ashes to Ashes / В прах обратишьс",
           "Название достижения: The Doppler Effect / Эффект Допплера",
           "Название достижения: Let the Good Times Roll! / Гуляй, душа!",
           "Название достижения: Shopaholic / Шопоголик",
           "Название достижения: Curator of Nightmares / Воплотившийся кошмар",
           "Название достижения: Curator of Nightmares / Воплотившийся кошмар",
           "Название достижения: Moo-rderer / Истребитель коров",
           "Название достижения: Rad Steez, Bro! / Экстремальный спорт",
           "Название достижения: The Grapes of Wrath Stomped / Вино из гроздьев ярости",
           "Название достижения: Hasta la Vista / Hasta la Vista",
           "Название достижения: David and Golyat / Давид и Голиаф",
        ]
        
        bot.send_message(message.chat.id, "Список скрытых достижений:\n" + "\n".join(hidden_achievements))
    elif achievement_name == "меню":
        # Отправить пользователю меню
        keyboard = create_keyboard()
        bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=keyboard)
    else:
        matching_achievements = [name for name in achievements_info if achievement_name in name.lower()]
        if matching_achievements:
            response = "\n".join([f"{name}:\n{achievements_info[name]}" for name in matching_achievements])
            bot.send_message(message.chat.id, response)
        else:
            bot.send_message(message.chat.id, "Достижение не найдено. Попробуйте еще раз.")

# Запускаем бота
bot.polling()
