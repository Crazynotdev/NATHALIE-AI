from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from src.core.ai import AIClient

class MessageHandler:
    def __init__(self, ai_client: AIClient):
        self.ai = ai_client

    async def handle_mention(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        response = await self.ai.generate(update.message.text)
        await update.message.reply_text(response)

    def register(self, app):
        app.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_mention)
        )
