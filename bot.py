
import telegram
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, MessageHandler, CommandHandler, \
                         CallbackContext, Filters, ChosenInlineResultHandler, \
                         InlineQueryHandler
from congig import TOKEN 

updater = Updater(TOKEN, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, давай пообщаемся?")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def textMessage(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Получил Ваше сообщение: ' + update.message.text)

text_handler = MessageHandler(Filters.text & (~Filters.command),textMessage)
dispatcher.add_handler(text_handler)


# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


updater.start_polling()