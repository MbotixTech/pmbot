from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = 'YOUR_TOKEN_BOT'
YOUR_GROUP_ID = -ID_GROUP  # Ganti dengan ID grup/channel Anda

def crot(update: Update, context):
    context.bot.forward_message(chat_id=YOUR_GROUP_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handlers
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, crot))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
