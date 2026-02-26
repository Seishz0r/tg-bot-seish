import os
import json
import threading
from flask import Flask
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# ==============================
# Flask (чтобы Render видел порт)
# ==============================

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ==============================
# Telegram Bot
# ==============================

TOKEN = os.getenv("BOT_TOKEN")

DATA_FILE = "tasks.json"


def load_tasks():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def save_tasks(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


users = load_tasks()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет 👋\n\n"
        "/add текст — добавить задачу\n"
        "/list — показать задачи\n"
        "/done номер — завершить задачу"
    )


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    text = " ".join(context.args)

    if not text:
        await update.message.reply_text("Напиши текст задачи после /add")
        return

    users.setdefault(user_id, [])
    users[user_id].append({"title": text, "completed": False})
    save_tasks(users)

    await update.message.reply_text("✅ Задача добавлена!")


async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    if user_id not in users or not users[user_id]:
        await update.message.reply_text("Список задач пуст.")
        return

    message = ""
    for i, task in enumerate(users[user_id], 1):
        status = "✅" if task["completed"] else "⬜"
        message += f"{i}. {status} {task['title']}\n"

    await update.message.reply_text(message)


async def done_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    if not context.args:
        await update.message.reply_text("Укажи номер задачи.")
        return

    try:
        index = int(context.args[0]) - 1
        users[user_id][index]["completed"] = True
        save_tasks(users)
        await update.message.reply_text("🎉 Задача выполнена!")
    except:
        await update.message.reply_text("Неверный номер задачи.")


def main():
    print("TOKEN:", TOKEN)

    if not TOKEN:
        raise ValueError("BOT_TOKEN не найден!")

    print("Starting bot...")

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_task))
    application.add_handler(CommandHandler("list", list_tasks))
    application.add_handler(CommandHandler("done", done_task))

    # Flask запускаем в отдельном потоке
    threading.Thread(target=run_web, daemon=True).start()

    # Бот запускаем в главном потоке (ВАЖНО!)
    application.run_polling()


if __name__ == "__main__":
    main()