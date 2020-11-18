import logging
import pickle
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)



logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

#Mensajes

archivo = open("mensajes.pickle", "rb")

saludo_m = pickle.load(archivo)
ayuda_m = pickle.load(archivo)
casos_m = pickle.load(archivo)
hospitales_m = pickle.load(archivo)
fallecidos_m = pickle.load(archivo)
#finde_m = pickle.load(archivo)
restricciones_m = pickle.load(archivo)
prevencion_m = pickle.load(archivo)
sintomas_m = pickle.load(archivo)

archivo.close()



#Stages
FIRST, SECOND = range(2)

#Callback data
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN = range(7)


def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Cifras 📊", callback_data=str(ONE))],
        [InlineKeyboardButton("Restricciones 🚫", callback_data=str(TWO))],
        [InlineKeyboardButton("Prevención 😷", callback_data=str(THREE))],
        [InlineKeyboardButton("Síntomas 🤒", callback_data=str(FOUR))]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(text=saludo_m, parse_mode="HTML", reply_markup=reply_markup)
    
    return FIRST


def start_over(update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Cifras 📊", callback_data=str(ONE))],
        [InlineKeyboardButton("Restricciones 🚫", callback_data=str(TWO))],
        [InlineKeyboardButton("Prevención 😷", callback_data=str(THREE))],
        [InlineKeyboardButton("Síntomas 🤒", callback_data=str(FOUR))]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=ayuda_m, parse_mode="HTML", reply_markup=reply_markup)

    return FIRST


def casos(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Situación hospitales 🏥", callback_data=str(SIX))],
        [InlineKeyboardButton("Fallecidos ✝", callback_data=str(SEVEN))]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=casos_m, parse_mode="HTML", reply_markup=reply_markup)

    return FIRST

def hospitales(update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Fallecidos ✝", callback_data=str(SEVEN))],
        [InlineKeyboardButton("Eskerrik Asko! 👍", callback_data=str(FIVE))]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=hospitales_m, parse_mode="HTML", reply_markup=reply_markup)

    return FIRST

def fallecidos(update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Situación hospitales 🏥", callback_data=str(SIX))],
        [InlineKeyboardButton("Eskerrik Asko! 👍", callback_data=str(FIVE))]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=fallecidos_m, parse_mode="HTML", reply_markup=reply_markup)

    return FIRST


def restricciones(update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Cifras 📊", callback_data=str(ONE))],
        [InlineKeyboardButton("Prevención 😷", callback_data=str(THREE))],
        [InlineKeyboardButton("Síntomas 🤒", callback_data=str(FOUR))],
        [InlineKeyboardButton("Eskerrik Asko! 👍", callback_data=str(FIVE))]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=restricciones_m, parse_mode="HTML", reply_markup=reply_markup)

    return FIRST

def prevencion(update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Cifras 📊", callback_data=str(ONE))],
        [InlineKeyboardButton("Restricciones 🚫", callback_data=str(TWO))],
        [InlineKeyboardButton("Síntomas 🤒", callback_data=str(FOUR))],
        [InlineKeyboardButton("Eskerrik Asko! 👍", callback_data=str(FIVE))]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=prevencion_m, parse_mode="HTML", reply_markup = reply_markup)

    return FIRST

def sintomas(update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Cifras 📊", callback_data=str(ONE))],
        [InlineKeyboardButton("Restricciones 🚫", callback_data=str(TWO))],
        [InlineKeyboardButton("Prevención 😷", callback_data=str(THREE))],
        [InlineKeyboardButton("Eskerrik Asko! 👍", callback_data=str(FIVE))]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=sintomas_m, parse_mode="HTML", reply_markup=reply_markup)

    return FIRST

def cierre(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Sí, necesito más información!", callback_data=str(ONE))],
        [InlineKeyboardButton("No, eskerrik asko!", callback_data=str(TWO))]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="¿Te puedo ayudar en algo más?", parse_mode="HTML", reply_markup=reply_markup)

    return SECOND

def end(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="¡Hasta la próxima!")
    return ConversationHandler.END


def main():
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler("start", start)],
        states = {
            FIRST: [
                CallbackQueryHandler(casos, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(restricciones, pattern="^" + str(TWO) + "$"),
                CallbackQueryHandler(prevencion, pattern="^" + str(THREE) + "$"),
                CallbackQueryHandler(sintomas, pattern="^" + str(FOUR) + "$"),
                CallbackQueryHandler(cierre, pattern="^" + str(FIVE) + "$"),
                CallbackQueryHandler(hospitales, pattern="^" + str(SIX) + "$"),
                CallbackQueryHandler(fallecidos, pattern="^" + str(SEVEN) + "$")
            ],
            SECOND: [
                CallbackQueryHandler(start_over, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(end, pattern="^" + str(TWO) + "$")
            ],
        },
        fallbacks=[CommandHandler("start", start)]
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()