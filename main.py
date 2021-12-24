import logging
import random

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (CommandHandler, Filters,
                          MessageHandler, Updater)

import config

# Массив результатов броска кубика
DICE = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣']

# Массив предсказаний
PREDICTIONS = [
    "🔮Ты всегда витаешь в облаках.",
    "🔮Не смотри так, у других тоже есть проблемы.",
    "🔮Никто не понимает, с какими проблемами ты столкнулся.",
    "🔮Дьявол скрытен.",
    "🔮Висельник не принесёт тебе удачи сегодня.",
    "🔮Ты делаешь ошибки, это нормально.",
    "🔮Твоя принцесса в другом замке.",
    "🔮Почему ты такой грустный?",
    "🔮Ты умрёшь.",
    "🔮Иди дальше.",
    "🔮Опасно ходить в одиночку.",
    "🔮Когда жизнь даёт тебе лимоны — сделай лимонад.",
    "🔮Следуй за кроликом.",
    "🔮Доверяй хорошим людям.",
    "🔮Не доверяй никому.",
    "🔮Не вини никого, кроме себя.",
    "🔮Не теряй голову.",
    "🔮Враньё.",
    "🔮Узри, что он узрел, делай то, что делал он.",
    "🔮Лишь грешник.",
    "🔮Не относись к людям предвзято.",
    "🔮Заведи питомца, он поднимет тебе настроение.",
    "🔮Всегда смотри на светлую сторону.",
    "🔮Ты видел выход?",
    "🔮Солнечные лучи на твоем личике.",
    "🔮Ну, это было бесполезно.",
    "🔮Не плачь на пролитые слёзы.",
    "🔮Счастливые числа: 16, 31, 64, 70, 74.",
    "🔮Отправляйся в тюрьму.",
    "🔮Верь в себя.",
    "🔮Перерождение было отменено.",
    "🔮Ты выглядишь толстым, тебе следует больше заниматься.",
    "🔮Принимай свои лекарства.",
    "🔮Выбери свой путь.",
    "🔮Твоя прежняя жизнь лежит в руинах.",
    "🔮Я чувствую, что сплю!!!",
    "🔮Твоих проблем может быть больше.",
    "🔮Следуй за собакой.",
    "🔮Следуй за кошкой.",
    "🔮Следуй за зеброй.",
    "🔮Что ты собираешься сегодня делать?",
    "🔮Используй бомбы с умом.",
    "🔮Живи, чтобы умереть.",
    "🔮Ты был неправльно рождён.",
    "🔮Тьма внутри тебя.",
    "🔮Ты никогда не будешь прощён.",
    "🔮Принеси ему фотокарточку.",
    "🔮Твоя душа сокрыта глубоко во тьме.",
    "🔮Ты умрёшь в одиночестве.",
    "🔮Смотри на луну.",
    "🔮Не покидай сегодня дом.",
    "🔮Все когда-нибудь умрут.",
    "🔮Ты прожигаешь свою жизнь.",
    "🔮Выйди на улицу!",
    "🔮Сдавайся!",
    "🔮Спроси позже.",
    "🔮Проснись.",
    "🔮Ты поклоняешься богу Солнца.",
    "🔮Спи.",
    "🔮Женитесь и размножайтесь.",
    "🔮Это вопрос компетенции.",
    "🔮Думай сам."
]

# Включение ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Функция построения меню из кнопок и количества столбцов
def build_menu(buttons, n_cols):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    return menu

# Ответ на комманду /start
def start(update, context):
    buttons = ["Бросить один кубик", "Бросить два кубика",
               "Подкинуть монетку", "Получить предсказание"]    # Массив кнопок
    reply_markup = ReplyKeyboardMarkup(build_menu(
        buttons, n_cols=2), resize_keyboard=True)               # Меню с изменяемым размером
    context.bot.send_message(chat_id=update.effective_chat.id,  # Отсылка сообщения с меню
                             text="Привет!\nЯ могу бросить кубики, подкинуть монетку и дать тебе предсказание\nЧто хочешь?",
                             reply_markup=reply_markup)

# Ответ на комманду /info
def info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Этот бот был создан на втором курсе университета для зачёта по дисциплине " +
                                  "\"Объектно-ориентированное программирование\".\n" +
                                  "У него нет практической пользы, да и оригинальной идеи для бота я не смог придумать, " +
                                  "но что есть - то есть.\nХорошего пользования ❤️")

# Функция броска одного кубик
def one_dice(update, context):
    reply_markup = ReplyKeyboardRemove(True)                                            # Меню = ничего
    context.bot.send_message(chat_id=update.effective_chat.id, text="Бросаю кубик!",
                             reply_markup=reply_markup)                                 # Отсылка сообщения с удалением меню
    # Случайное число >=0 <=5
    value = random.randint(0, 5)
    # Отсылка сообщения с результатом
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=DICE[value]+"🎲")

    # Создание меню и отсылка сообщения с меню
    buttons = ["Бросить один кубик", "Бросить два кубика",
               "Подкинуть монетку", "Получить предсказание"]
    reply_markup = ReplyKeyboardMarkup(
        build_menu(buttons, n_cols=2), resize_keyboard=True)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Что дальше?", reply_markup=reply_markup)

# Функция броска двух кубиков
def two_dices(update, context):
    reply_markup = ReplyKeyboardRemove(True)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Бросаю кубики!", reply_markup=reply_markup)
    value = random.randint(0, 5)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=DICE[value]+"🎲")
    value = random.randint(0, 5)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=DICE[value]+"🎲")

    buttons = ["Бросить один кубик", "Бросить два кубика",
               "Подкинуть монетку", "Получить предсказание"]
    reply_markup = ReplyKeyboardMarkup(
        build_menu(buttons, n_cols=2), resize_keyboard=True)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Что дальше?", reply_markup=reply_markup)

# Функция броска монеты
def coin_flip(update, context):
    reply_markup = ReplyKeyboardRemove(True)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Подбрасываю монетку!", reply_markup=reply_markup)
    # Случайное значние из предложенных
    value = random.choice([True, False])

    # Проверка значения
    if(value):
        context.bot.send_animation(chat_id=update.effective_chat.id, animation=open(    # Отсылка анимации с подписью,
            'gifs\heads.gif', 'rb'), caption="Выпал орёл!")                             # если значение True
    else:
        context.bot.send_animation(chat_id=update.effective_chat.id, animation=open(    # Если значение False
            'gifs\\tails.gif', 'rb'), caption="Выпала решка!")

    buttons = ["Бросить один кубик", "Бросить два кубика",
               "Подкинуть монетку", "Получить предсказание"]
    reply_markup = ReplyKeyboardMarkup(
        build_menu(buttons, n_cols=2), resize_keyboard=True)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Что дальше?", reply_markup=reply_markup)

# Функция получения предсказания
def prediction(update, context):
    reply_markup = ReplyKeyboardRemove(True)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Генерирую предсказание!", reply_markup=reply_markup)
    # Случайное предсказание из 62
    value = random.randint(0, 61)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=PREDICTIONS[value])

    buttons = ["Бросить один кубик", "Бросить два кубика",
               "Подкинуть монетку", "Получить предсказание"]
    reply_markup = ReplyKeyboardMarkup(
        build_menu(buttons, n_cols=2), resize_keyboard=True)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Что дальше?", reply_markup=reply_markup)


# Получение информации от бота по токену
updater = Updater(config.TOKEN)
# Создание обработчика сообщений
dispatcher = updater.dispatcher

# Создание обработчика комманды /start
start_handler = CommandHandler("start", start)
# Добавление обработчика в обработчика сообщений
dispatcher.add_handler(start_handler)

info_handler = CommandHandler("info", info)
dispatcher.add_handler(info_handler)

# Создание обработчика сообщения, содержащего "Бросить один кубик"
one_dice_handler = MessageHandler(
    Filters.regex("Бросить один кубик"), one_dice)
dispatcher.add_handler(one_dice_handler)

two_dices_handler = MessageHandler(
    Filters.regex("Бросить два кубика"), two_dices)
dispatcher.add_handler(two_dices_handler)

coin_flip_handler = MessageHandler(
    Filters.regex('Подкинуть монетку'), coin_flip)
dispatcher.add_handler(coin_flip_handler)

prediction_handler = MessageHandler(
    Filters.regex("Получить предсказание"), prediction)
dispatcher.add_handler(prediction_handler)

# Включение получения обновлений
updater.start_polling()
# Ожидание отключения ботa с помощью ^C
updater.idle()
