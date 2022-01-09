import api as keys
from telegram.ext import *
import Responses as R

print("Bot started")


def start(update, context):
    update.message.reply_text('Hello, I am Snappy')


def help(update, context):
    update.message.reply_text("""
    The following commands are available:

    /start -> Welcome Message
    /help -> This Message
    /contact -> Ways to contact
    """)

def contact(update,context):
    update.message.reply_text("You can contact my creator Chirag Malik on his email address itschiragmalik@gmail.com")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("contact", contact))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
