import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "BOT"
API_URL = " URL"  # или ваш домен


# Команда: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот, связанный с сайтом. Используй /mytasks чтобы посмотреть задачи.")


# Команда: /mytasks
async def mytasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # 🔽 Запрос к сайту (FastAPI) — получаем задачи пользователя
    response = requests.get(f"{API_URL}/get_by_telegram_id/{user_id}")

    if response.status_code == 200:
        tasks = response.json()
        if tasks:
            message = "\n\n".join(f"📌 {t['title']}: {t['description']}" for t in tasks)
        else:
            message = "Задачи не найдены."
    else:
        message = "Ошибка получения данных с сайта."

    await update.message.reply_text(message)


# Запуск бота
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("mytasks", mytasks))

if __name__ == "__main__":
    app.run_polling()
