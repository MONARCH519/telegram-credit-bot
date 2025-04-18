from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# 🔐 Токен Telegram-бота
TOKEN = "7645634931:AAGyLcBr4IdbZwAGOXfX4-DTMGZWmN6Cbqk"

# 🔹 Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Информация", "Документы"],
        ["Связь с оператором"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Привет! Добро пожаловать в нашего телеграм-бота по кредитным вопросам.\n\n"
        "Выберите нужный раздел ниже 👇",
        reply_markup=reply_markup
    )

# 🔹 Ответы на кнопки
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "информация":
        await update.message.reply_text(
            "📄 1. Кредитные компании требуют от вас:\n"
            "- Постоянное место работы (арбайт, официалка — не важно)\n"
            "- Зарплата должна поступать на счёт в течение последних 3 месяцев\n\n"
            "📄 2. Наши условия как связных операторов:\n"
            "- Вы даёте согласие на рассмотрение своих личных данных для подачи заявки\n"
            "- После одобрения кредита вы оплачиваете наши услуги — 10% от суммы"
        )

    elif text == "документы":
        await update.message.reply_text(
            "📁 Документы, которые нужно подготовить:\n\n"
            "1. Фото айди-карты с двух сторон\n"
            "2. Адрес проживания\n"
            "3. Виза\n"
            "4. Номер телефона\n"
            "5. Место работы (название завода/компании)\n"
            "6. Адрес места работы\n"
            "7. Официальное ли трудоустройство\n"
            "8. Есть ли 4 вида страховки\n"
            "9. Срок работы\n"
            "10. Есть ли задолженности (если есть — указать сумму)\n"
            "11. Зарплата в месяц\n"
            "12. Кредитный рейтинг\n\n"
            "📝 P.S. Если понадобятся дополнительные документы — мы сообщим и дополним список."
        )

    elif text == "связь с оператором":
        keyboard = [
            [InlineKeyboardButton("💬 Написать оператору", url="https://t.me/creditkorea993")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "📞 Если вас всё устраивает, вы можете сразу связаться с оператором по кнопке:",
            reply_markup=reply_markup
        )

    else:
        await update.message.reply_text("🤔 Я не понимаю эту команду. Пожалуйста, используйте кнопки ниже 👇")

# 🔹 Запуск бота
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ Бот запущен!")
app.run_polling()
