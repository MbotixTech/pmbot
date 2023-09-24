from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = 'YOUR_TOKEN_BOT'
YOUR_GROUP_ID = -ID_GROUP  # Yout group id

def crot(update: Update, context):
    context.bot.forward_message(chat_id=YOUR_GROUP_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, crot))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
