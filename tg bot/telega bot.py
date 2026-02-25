from telegram import Update
import json
import os


from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

import os
TOKEN = os.getenv("BOT_TOKEN")

# Хранилище задач по user_id
users = {}


class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "⬜"
        return f"{status} {self.title}"


# --- Команды ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    users[user_id] = []
    await update.message.reply_text(
        "Привет! 👋\n"
        "Просто напиши задачу — я её добавлю.\n\n"
        "Команды:\n"
        "/show — показать задачи\n"
        "/delete N — удалить задачу\n"
        "/done N — завершить задачу"
    )


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if user_id not in users:
        users[user_id] = []

    users[user_id].append(Task(text))
    save_data()
    await update.message.reply_text("✅ Задача добавлена!")


async def show_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in users or not users[user_id]:
        await update.message.reply_text("Список задач пуст.")
        return

    tasks_text = "\n".join(
        f"{i+1}. {task}" for i, task in enumerate(users[user_id])
    )

    await update.message.reply_text(tasks_text)


async def delete_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in users or not users[user_id]:
        await update.message.reply_text("Список задач пуст.")
        return

    if not context.args:
        await update.message.reply_text("Используй: /delete номер")
        return

    try:
        index = int(context.args[0]) - 1
        removed = users[user_id].pop(index)
        save_data()
        await update.message.reply_text(f"Удалена задача: {removed.title}")
    except ValueError:
        await update.message.reply_text("Номер должен быть числом!")
    except IndexError:
        await update.message.reply_text("Задачи с таким номером нет!")


async def complete_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in users or not users[user_id]:
        await update.message.reply_text("Список задач пуст.")
        return

    if not context.args:
        await update.message.reply_text("Используй: /done номер")
        return

    try:
        index = int(context.args[0]) - 1
        users[user_id][index].mark_done()
        save_data()
        await update.message.reply_text("✅ Задача отмечена выполненной!")
    except ValueError:
        await update.message.reply_text("Номер должен быть числом!")
    except IndexError:
        await update.message.reply_text("Задачи с таким номером нет!")


def save_data():
    data = {}

    for user_id, tasks in users.items():
        data[user_id] = [
            {"title": task.title, "completed": task.completed}
            for task in tasks
        ]

    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_data():
    if not os.path.exists("tasks.json"):
        return

    with open("tasks.json", "r", encoding="utf-8") as f:
        data = json.load(f)

        for user_id, tasks in data.items():
            users[int(user_id)] = [
                Task(task["title"], task["completed"])
                for task in tasks
            ]

# --- Запуск бота ---

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("show", show_tasks))
app.add_handler(CommandHandler("delete", delete_task))
app.add_handler(CommandHandler("done", complete_task))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, add_task))

load_data()

app.run_polling()