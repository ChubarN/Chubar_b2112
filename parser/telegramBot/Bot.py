#Nazar_Chubar_bot.
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

list_commands = ""

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def say1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v)

    async def say2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.(v)

        async def verse2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            await update.message.(v)


app = ApplicationBuilder().token("7576354868:AAHHlNvMGBtF_pC67tGKIzCKItEQYudwTO4").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("say1", say1))
app.add_handler(CommandHandler("verse2", verse2))
app.run_polling()