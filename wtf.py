
import telegram
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext, Filters, ChosenInlineResultHandler
from config import TOKEN

bot = telegram.Bot(TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

def get_inline_results(bot, update):
    query = update.inline_query.query
    results = list()

    results.append(InlineQueryResultArticle(id='1000',
                                            title="Book 1",
                                            description='Description of this book, author ...',
                                            thumb_url='https://fakeimg.pl/100/?text=book%201',
                                            input_message_content=InputTextMessageContent(
                                                'chosen book:')))

    results.append(InlineQueryResultArticle(id='1001',
                                            title="Book 2",
                                            description='Description of the book, author...',
                                            thumb_url='https://fakeimg.pl/300/?text=book%202',
                                            input_message_content=InputTextMessageContent(
                                                'chosen book:')
                                            ))

    update.inline_query.answer(results)


inline_query_handler = InlineQueryHandler(get_inline_results)
dispatcher.add_handler(inline_query_handler)

def on_result_chosen(bot, update):
    print(update.to_dict())
    result = update.chosen_inline_result
    result_id = result.result_id
    query = result.query
    user = result.from_user.id
    print(result_id)
    print(user)
    print(query)
    print(result.inline_message_id)
    bot.send_message(user, text='fetching book data with id:' + result_id)


result_chosen_handler = ChosenInlineResultHandler(on_result_chosen)
dispatcher.add_handler(result_chosen_handler)