from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8314362212:AAEJs2qVZ3ETUulVqe5d-90QYtUi_ChkHZk"          # ← paste from @BotFather
WEBAPP_URL = "https://lowercase-sable.vercel.app/"   # ← your deployed index.html

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Open Wallet → Connect",
        reply_markup={
            "inline_keyboard": [[{
                "text": "Open Wallet Connect",
                "web_app": {"url": WEBAPP_URL}
            }]]
        }
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()